from pathlib import Path
import json,re,math
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pptx import Presentation
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN
from lxml import etree
from PIL import ImageFont
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'arabic'
source=json.loads((OUT/'source-strings.json').read_text()); resolved=json.loads((OUT/'resolved-translations.json').read_text())
T={v['text']:resolved[str(v['id'])] for v in source}
FONT='IBM Plex Sans Arabic'
fontpath=Path.home()/'.local/share/fonts/pmp/IBMPlexSansArabic-Regular.ttf'
missing=set()
def tr(s):
 if not s.strip():return s
 if s in T:return T[s]
 missing.add(s);return s
FILES=['handover/PMP-Marketing-Department-Owner-Handover-SOP.docx','onboarding/PMP-Incoming-Marketing-Manager-Detailed-Runbook.docx','handover/PMP-Marketing-Department-Owner-Handover.pptx','onboarding/PMP-Incoming-Marketing-Manager-Detailed-Onboarding.pptx','presentations/PMP-Growth-OS-Full-Client-Journey-Editable.pptx']
def docpara(p):
 old=p.text
 if old.strip():
  translated=tr(old)
  texts=p._p.xpath('.//w:t')
  if texts:
   texts[0].text=translated
   for t in texts[1:]:t.text=''
 pp=p._p.get_or_add_pPr(); bidi=OxmlElement('w:bidi');bidi.set(qn('w:val'),'1');pp.append(bidi)
 p.alignment=WD_ALIGN_PARAGRAPH.RIGHT
 for run in p.runs:
  run.font.name=FONT
  rp=run._r.get_or_add_rPr();rf=rp.rFonts
  if rf is not None:
   for name in ['ascii','hAnsi','cs','eastAsia']:rf.set(qn('w:'+name),FONT)
  rt=OxmlElement('w:rtl');rt.set(qn('w:val'),'1');rp.append(rt)
def docwalk(container):
 for p in container.paragraphs:docpara(p)
 for table in container.tables:
  prop=table._tbl.tblPr;el=OxmlElement('w:bidiVisual');prop.append(el)
  seen=set()
  for row in table.rows:
   for cell in row.cells:
    if cell._tc not in seen:seen.add(cell._tc);docwalk(cell)
def fitframe(shape):
 tf=shape.text_frame
 width=max(10,(shape.width-tf.margin_left-tf.margin_right)/914400*72)
 height=max(8,(shape.height-tf.margin_top-tf.margin_bottom)/914400*72)
 sizes=[r.font.size.pt for p in tf.paragraphs for r in p.runs if r.font.size]
 size=min(max(sizes or [16]),28)
 def need(sz):
  font=ImageFont.truetype(str(fontpath),max(1,int(sz*2)))
  total=0
  for p in tf.paragraphs:
   line=0;lines=1
   for word in p.text.split():
    advance=font.getlength(word+' ')/2
    if line+advance>width and line:lines+=1;line=advance
    else:line+=advance
   total+=lines*sz*1.38+(p.space_after.pt if p.space_after else 0)
  return total
 while size>8 and need(size)>height:size-=.5
 for p in tf.paragraphs:
  p.alignment=PP_ALIGN.RIGHT;p._p.get_or_add_pPr().set('rtl','1')
  for r in p.runs:r.font.name=FONT;r.font.size=Pt(size)
for filename in FILES:
 src=ROOT/filename;dest=OUT/(src.stem+'-AR'+src.suffix)
 if src.suffix=='.docx':
  d=Document(src);docwalk(d)
  for sec in d.sections:docwalk(sec.header);docwalk(sec.footer)
  for style in d.styles:
   if hasattr(style,'font'):style.font.name=FONT
  d.save(dest)
  # Companion editable plain text, complete paragraph and table content.
  content=[p.text for p in d.paragraphs]
  content += [' | '.join(c.text for c in row.cells) for t in d.tables for row in t.rows]
  dest.with_suffix('.md').write_text('\n\n'.join(content))
 else:
  deck=Presentation(src)
  for slide in deck.slides:
   for shape in slide.shapes:
    shape.left=deck.slide_width-shape.left-shape.width
    if shape.shape_type==9:
     for x in shape._element.xpath('.//a:xfrm'):x.set('flipH','0' if x.get('flipH')=='1' else '1')
    if shape.has_text_frame:
     for p in shape.text_frame.paragraphs:
      translated=tr(p.text)
      if p.runs:
       p.runs[0].text=translated
       for r in p.runs[1:]:r.text=''
      elif translated:p.text=translated
     fitframe(shape)
   if slide.has_notes_slide:
    for p in slide.notes_slide.notes_text_frame.paragraphs:
     translated=tr(p.text)
     if p.runs:
      p.runs[0].text=translated
      for r in p.runs[1:]:r.text=''
     elif translated:p.text=translated
  deck.save(dest)
 print(dest.name)
(OUT/'unmatched-strings.json').write_text(json.dumps(sorted(missing),ensure_ascii=False,indent=2))
assert not missing, f'{len(missing)} untranslated paragraphs'
