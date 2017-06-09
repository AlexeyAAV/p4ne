import glob
import re
flist=glob.iglob(r"C:\Users\Anastasiev\Desktop\Seafile libs\Seafile\p4ne_training\config_files\*.txt")
ip = []
int = []
for i in flist:
    with open(i) as f:
        for line in f:
            if re.match('^(.+?)ip address(.+?)$', line):
                ip.append(line.strip())
            if re.match('^(.+?)INT(.+?)$', line):
                int.append(line.strip())

ip  = list(set(ip))
print(ip)
int  = list(set(int))
print(int)