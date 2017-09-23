import re

name = r"filename"
floder = r"filepath"
newname = "new@" + name
path = floder + '\\' + name
newpath = floder + '\\' + newname
order = open (path).readlines ()
for sequencing  in order:
    dna = re.findall (r"TGGAATTGCCCTT(.+?)AAGGGCAATT", sequencing)
new = open (newpath, 'w')
for dnaorder in dna:
    new.write (dnaorder)
