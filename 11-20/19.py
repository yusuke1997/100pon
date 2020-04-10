f=open("hightemp.txt")

data=set()
data1=list()
for i in f:
    line=i.split("\t")
    data.add(line[0])
    data1.append(line[0])

datas=[]
for i in data:
    datas.append([i,0])

for i in data1:
    line=i.split("\t")
    for j in datas:
        if(j[0]==line[0]):
            j[1]+=1
            continue

datas=sorted(datas,key=lambda x: x[1],reverse=True)
for i in datas:
    print(i[0]+" "+str(i[1]))
    

