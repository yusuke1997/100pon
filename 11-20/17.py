f=open("hightemp.txt")

data=set()
for i in f:
    line=i.split("\t")
    data.add(line[0])

for i in data:
    print(i)
