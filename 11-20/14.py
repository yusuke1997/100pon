import sys

argv=sys.argv

#print(argv)
if(len(argv)!=2):
    print("error")
    exit()

f=open("hightemp.txt")

for i in range(int(argv[1])):
    line=f.readline()
    print(line,end="")
