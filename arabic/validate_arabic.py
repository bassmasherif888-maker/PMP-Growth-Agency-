from pathlib import Path
from zipfile import ZipFile
from html.parser import HTMLParser
from pptx import Presentation
from docx import Document
import json,fitz
r=Path(__file__).resolve().parent
assert json.loads((r/'pending-translations.json').read_text())==[]
assert json.loads((r/'unmatched-strings.json').read_text())==[]
for f in list(r.glob('*.docx'))+list(r.glob('*.pptx')):
 with ZipFile(f) as z:assert z.testzip() is None
 pdf=fitz.open(f.with_suffix('.pdf'))
 assert all(len(p.get_text().strip())>100 for p in pdf)
 if f.suffix=='.pptx':
  d=Presentation(f);assert len(d.slides)==len(pdf)
  assert not any(s.shape_type==13 for p in d.slides for s in p.shapes)
 else:
  d=Document(f)
  assert all(p._p.xpath('./w:pPr/w:bidi') for p in d.paragraphs)
 print(f.name, len(pdf),'rendered pages')
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  if tag=='a':
   href=dict(attrs)['href'];assert (r/href).is_file(),href
Links().feed((r/'index.html').read_text())
print('PASS: complete translation coverage; editable native Office files; RTL Word paragraphs; PDFs; bilingual download links.')
