target=open("hightemp.txt")

for i in target:
    i=i.replace("\t"," ")
    print(i,end="")
