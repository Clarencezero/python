import re

key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
p1 = "\bhref=\"\([^\"]*)"
pattern1 = re.compile(p1)
print(pattern1.findall(key))
