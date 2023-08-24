from collections import OrderedDict
def printer(s:str):
  d = OrderedDict()
  for c in s.upper():
    if c != ' ':
      d.setdefault(c,0)
      d[c]+=1
  k = [i for i in d.keys()]
  k.sort()
  for x in k:
    print(x, d[x])

printer("Hello welcome to Cathay 60th year anniversary")
