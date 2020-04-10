target=open("hightemp.txt")

col1=open("col1.txt","w")
col2=open("col2.txt","w")

for i in target:
    a=i.split("\t")
    col1.write(a[0]+"\n")
    col2.write(a[1]+"\n")

