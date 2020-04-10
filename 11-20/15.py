import sys

argv=sys.argv

#print(argv)
if(len(argv)!=2):
    print("error")
    exit()

f=open("hightemp.txt")

lines=f.readlines()
#print(lines)
for i in range(min(int(argv[1]),len(lines)),0,-1):
    print(lines[i*(-1)],end="")

