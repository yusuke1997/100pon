f=open("hightemp.txt")

datas=f.readlines()

data=[]
for i in datas:
  data.append(i.replace("\n","").split("\t"))

data=sorted(data,key=lambda x: x[2],reverse=True)

for i in data:
    print(i)
