col1=open("col1.txt")
col2=open("col2.txt")

f=open("test_hightemp.txt","w")

for i,j in zip(col1,col2):
    col=i.replace("\n","")+"\t"+j
    f.write(col)
    
