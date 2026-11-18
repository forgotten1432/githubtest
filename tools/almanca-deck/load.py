import glob, re, sys
def load(d='data'):
    entries=[]; seen={}; dupes=[]; bad=[]
    for f in sorted(glob.glob(d+'/*.txt')):
        tag='Allgemein'
        for ln,line in enumerate(open(f,encoding='utf-8'),1):
            line=line.rstrip('\n')
            if not line.strip(): continue
            if line.startswith('#'): tag=line[1:].strip().replace(' ','_'); continue
            p=line.split('|')
            if len(p)!=6: bad.append((f,ln,line)); continue
            k,art,w,extra,tr,ex=[x.strip() for x in p]
            key=(art, w.lower() if k in ('adv','int','adj','conj','prep','num') else w, 'v' if k=='v' else 'x')
            if key in seen: dupes.append((f,ln,art,w)); continue
            seen[key]=1
            entries.append(dict(kind=k,art=art,word=w,extra=extra,tr=tr,ex=ex,tag=tag,file=f))
    return entries,dupes,bad
if __name__=='__main__':
    e,d,b=load()
    print(len(e),'unique;',len(d),'dupes;',len(b),'bad')
    for x in b: print('BAD',x)
    print([ (a,w) for _,_,a,w in d])
    from collections import Counter
    print(Counter(x['kind'] for x in e))
