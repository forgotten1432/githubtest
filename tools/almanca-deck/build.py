import sys, html
sys.path.insert(0,'.')
import genanki
from load import load
import glob as _g
UG={}
for _f in sorted(_g.glob('ug/*.txt')):
    for _l in open(_f,encoding='utf-8'):
        _l=_l.rstrip('\n')
        if _l.strip():
            _k,_v=_l.split('|',1); UG.setdefault(_k.strip(),_v.strip())
NT={}
for _f in sorted(_g.glob('notes/*.txt')):
    for _l in open(_f,encoding='utf-8'):
        _l=_l.rstrip('\n')
        if _l.strip():
            _k,_t,_u=_l.split('|'); NT[_k.strip()]=(_t.strip(),_u.strip())
import re as _re
def bidi(t):
    L=r'[A-Za-zÄÖÜäöüß]'
    out=[]
    for part in _re.split(r'(«[^»]*»)',t):
        if part.startswith('«') and part.endswith('»'):
            inner=part[1:-1]
            out.append('«<bdi dir="ltr">'+inner+'</bdi>»' if _re.search(L,inner) else part)
        else:
            out.append(_re.sub(r'(%s[\wÄÖÜäöüß\-]*(?:[ /]%s[\wÄÖÜäöüß\-]*)*)'%(L,L),r'<bdi dir="ltr">\1</bdi>',part))
    return ''.join(out)
def note_for(x):
    full=(x['art']+' '+x['word']).strip()
    return NT.get(x['kind']+':'+full) or NT.get(full) or ('','')
def ug_for(x):
    full=(x['art']+' '+x['word']).strip()
    return UG.get(x['kind']+':'+full) or UG.get(full) or ''

entries, dupes, bad = load()
assert not bad

KIND = {'n':'isim','v':'fiil','adj':'sıfat','adv':'zarf','int':'kalıp / ünlem','num':'sayı',
        'prep':'edat','pron':'zamir','conj':'bağlaç','det':'belirteç'}
FORMS_LABEL = {'v':'er/sie/es · Präteritum · Perfekt','adj':'Komparativ · Superlativ','n':'Çoğul'}

CSS = """
.card{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;font-size:22px;text-align:center;color:#222;background:#fff;padding:12px}
.nightMode .card,.night_mode .card{color:#eee;background:#1e1e1e}
.word{font-size:40px;font-weight:600;margin:14px 0 6px}
.art{font-weight:400;margin-right:.25em}
.der{color:#1e6bd6}.die{color:#d6336c}.das{color:#2f9e44}
.kind{display:inline-block;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:#777;border:1px solid #bbb;border-radius:10px;padding:1px 9px;margin-top:4px}
.tr{font-size:32px;font-weight:600;margin:12px 0 4px}
.forms{font-size:20px;color:#444;margin-top:12px}
.nightMode .forms,.night_mode .forms{color:#ccc}
.flabel{display:block;font-size:12px;color:#888;text-transform:uppercase;letter-spacing:.04em}
.hint{font-size:15px;color:#999;margin-top:8px}
.ug{font-family:"UKIJ Tuz Tom","Noto Naskh Arabic","Geeza Pro",serif;font-size:24px;color:#8a4b08;direction:rtl;margin:2px 0 4px}
.nightMode .ug,.night_mode .ug{color:#f0b46a}
.note{text-align:left;font-size:16px;line-height:1.45;margin:14px auto 0;padding:10px 12px;border-radius:10px;background:#f6f3ea;color:#3d3528;max-width:34em}
.note .nl{display:block;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#9a8a6a;margin-bottom:3px}
.note .ugn{direction:rtl;text-align:right;font-family:"UKIJ Tuz Tom","Noto Naskh Arabic","Geeza Pro",serif;font-size:17px;margin-top:8px;padding-top:8px;border-top:1px dashed #d8ccb0}
.nightMode .note,.night_mode .note{background:#2c2a24;color:#e8dfcc}
.ex{font-size:19px;font-style:italic;color:#555;margin-top:14px}
.nightMode .ex,.night_mode .ex{color:#bbb}
hr#answer{margin:14px 0;border:0;border-top:1px solid #ddd}
"""

FRONT_DE = """<div class="word">{{#Artikel}}<span class="art {{Artikel}}">{{Artikel}}</span>{{/Artikel}}<span class="{{Artikel}}">{{Wort}}</span></div>
<div class="kind">{{Tür}}</div>"""
BACK_DE = """{{FrontSide}}<hr id="answer">
<div class="tr">{{Türkçe}}</div>
{{#Uygurca}}<div class="ug" dir="rtl" lang="ug">{{Uygurca}}</div>{{/Uygurca}}
{{#Formen}}<div class="forms"><span class="flabel">{{FormenLabel}}</span>{{Formen}}</div>{{/Formen}}
<div class="ex">{{Beispiel}}</div>
{{#Açıklama}}<div class="note"><span class="nl">Açıklama · ئىزاھات</span>{{Açıklama}}{{#Izahat}}<div class="ugn" dir="rtl" lang="ug">{{Izahat}}</div>{{/Izahat}}</div>{{/Açıklama}}"""

FRONT_TR = """<div class="tr">{{Türkçe}}</div>
{{#Uygurca}}<div class="ug" dir="rtl" lang="ug">{{Uygurca}}</div>{{/Uygurca}}
<div class="kind">{{Tür}}</div>
{{#Hinweis}}<div class="hint">ipucu: {{Hinweis}}</div>{{/Hinweis}}"""
BACK_TR = """{{FrontSide}}<hr id="answer">
<div class="word">{{#Artikel}}<span class="art {{Artikel}}">{{Artikel}}</span>{{/Artikel}}<span class="{{Artikel}}">{{Wort}}</span></div>
{{#Formen}}<div class="forms"><span class="flabel">{{FormenLabel}}</span>{{Formen}}</div>{{/Formen}}
<div class="ex">{{Beispiel}}</div>
{{#Açıklama}}<div class="note"><span class="nl">Açıklama · ئىزاھات</span>{{Açıklama}}{{#Izahat}}<div class="ugn" dir="rtl" lang="ug">{{Izahat}}</div>{{/Izahat}}</div>{{/Açıklama}}"""

MODEL_ID = 1607392319
DECK_ID = 2059400118
model = genanki.Model(
    MODEL_ID, 'Almanca Temel Sözcük (DE-TR)',
    fields=[{'name':n} for n in ['Sıra','Artikel','Wort','Tür','Türkçe','FormenLabel','Formen','Beispiel','Hinweis','Uygurca','Açıklama','Izahat']],
    templates=[
        {'name':'Almanca → Türkçe','qfmt':FRONT_DE,'afmt':BACK_DE},
        {'name':'Türkçe → Almanca','qfmt':FRONT_TR,'afmt':BACK_TR},
    ], css=CSS)

deck = genanki.Deck(DECK_ID, 'Almanca – Temel 2000 Sözcük')
e = html.escape
import collections
trcount = collections.Counter(x['tr'] for x in entries)
for i,x in enumerate(entries,1):
    forms = x['extra']
    if forms in ('–','-',''): forms=''
    label = FORMS_LABEL.get(x['kind'],'')
    if x['kind']=='n' and forms:
        forms = ('die ' if x['art']!='' else '') + forms   # plural article
        # plurals like "Tische" -> "die Tische"
    fields = [f"{i:04d}", e(x['art']), e(x['word']), KIND[x['kind']], e(x['tr']),
              label if forms else '', e(forms), e(x['ex']),
              (e((x['art']+' ' if x['art'] else '')+x['word'][:2]+'…') if trcount[x['tr']]>1 else ''),
              e(ug_for(x)), e(note_for(x)[0]), bidi(e(note_for(x)[1]))]
    tags = [x['tag'], 'Temel2000', x['kind']]
    deck.add_note(genanki.Note(model=model, fields=fields, tags=tags,
                               guid=genanki.guid_for('de2000', x['art'], x['word'], x['kind']), sort_field=0))
pkg = genanki.Package(deck)
pkg.write_to_file(sys.argv[1] if len(sys.argv)>1 else 'Almanca_Temel_2000_Sozcuk.apkg')
print(len(entries),'notes ->',len(entries)*2,'cards')
