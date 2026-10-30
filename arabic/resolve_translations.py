from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
items=json.loads((ROOT/'source-strings.json').read_text());auto=json.loads((ROOT/'auto-translations.json').read_text());manual={}
for line in (ROOT/'translations.txt').read_text().splitlines():
 if '|' in line:
  k,v=line.split('|',1);manual[k]=v.replace(' ⏎ ','\n')
resolved={**auto,**manual}
def norm(t):return re.sub(r'\s+',' ',t).strip().casefold().replace('’',"'").replace('—','-')
for _ in range(5):
 known={norm(i['text']):resolved[str(i['id'])] for i in items if str(i['id']) in resolved}
 # Strip only explicit wrappers; never change operational meaning.
 wrappers=[('• ','• '),('Core work: ','جوهر الدور: '),('Expected evidence: ','الأدلة المتوقعة: '),('Expected daily/work-cycle evidence: ','الأدلة اليومية/الدورية: '),('Reporting: ','التبعية: '),('Reporting relation: ','التبعية: '),('Procedure gate: ','شرط الإجراء: '),('Gate: ','شرط الانتقال: '),('Required record: ','السجل المطلوب: '),('Output: ','المخرج: ')]
 stripped={}
 for i in items:
  if str(i['id']) not in resolved:continue
  src=i['text'];dst=resolved[str(i['id'])]
  for prefix,ar in wrappers:
   if src.startswith(prefix) and dst.startswith(ar):stripped[norm(src[len(prefix):])]=dst[len(ar):]
  m=re.match(r'^(\d+[. /]+)(.*)',src,re.S)
  if m:
   n=re.match(r'^\d+[. /]+(.*)',dst,re.S)
   if n:stripped[norm(m.group(2))]=n.group(1)
 for i in items:
  k=str(i['id']);src=i['text']
  if k in resolved:continue
  if norm(src) in known:resolved[k]=known[norm(src)];continue
  if norm(src) in stripped:resolved[k]=stripped[norm(src)];continue
  for prefix,ar in wrappers:
   if src.startswith(prefix) and norm(src[len(prefix):]) in known:
    resolved[k]=ar+known[norm(src[len(prefix):])];break
  if k in resolved:continue
  parts=src.split('\n')
  if len(parts)>1 and all(norm(p) in known or not re.search('[A-Za-z]{2}',p) for p in parts):resolved[k]='\n'.join(known.get(norm(p),p) for p in parts)
(ROOT/'resolved-translations.json').write_text(json.dumps(resolved,ensure_ascii=False,indent=2)+'\n')
pending=[i for i in items if str(i['id']) not in resolved]
(ROOT/'pending-translations.json').write_text(json.dumps(pending,ensure_ascii=False,indent=2)+'\n')
for n in range(0,len(pending),180):Path(f'/tmp/ar-pending-{n//180+1}.txt').write_text('\n'.join(str(i['id'])+'|'+i['text'].replace('\n',' ⏎ ') for i in pending[n:n+180]))
print('Resolved',len(resolved),'Pending',len(pending),'Remaining words',sum(len(i['text'].split()) for i in pending))
