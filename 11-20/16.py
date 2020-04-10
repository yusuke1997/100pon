import sys
import math

argv=sys.argv

#print(argv)
if(len(argv)!=2):
    print("error")
    exit()

f=open("hightemp.txt")

lines=f.readlines()

path="./child/"

length=len(lines)
batch=int(math.ceil(length/int(argv[1])))

print(batch)

num=0

while(len(lines)>0):
    whitedata=lines[:batch]
    lines=lines[batch:]
    w=open(path+"child"+str(num)+".txt","w")
    for i in whitedata:
        w.write(i)
    num+=1
