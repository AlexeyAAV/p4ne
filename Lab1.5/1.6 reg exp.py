import glob
import re
flist=glob.iglob(r"C:\Users\Anastasiev\Desktop\Seafile libs\Seafile\p4ne_training\config_files\*.txt")
l = []
for i in flist:
    with open(i) as f:
        for line in f:
            if re.match('^(.+?)ip address(.+?)$', line):
                l.append(line.strip())

l  = list(set(l))
print(l)