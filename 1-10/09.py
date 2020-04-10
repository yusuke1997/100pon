import random

tar="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

tar2=tar.split(" ")

res=[]
for i in tar2:
    if(len(i)<=4):
        res.append(i)
    else:
        word=i[0]
        between=list(i[1:-1])
        random.shuffle(between)
        word+="".join(between)
        word+=i[-1]
        res.append(word)

print(" ".join(res))
