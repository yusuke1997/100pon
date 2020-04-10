tar="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dictmap={}

tar=tar.replace(",","").replace(".","").replace("'","")

target=tar.split(" ")

for i,word in enumerate(target):
    i+=1
    if(i in [1,5,6,7,8,9,15,16,19]):
        dictmap[word[0]]=i
    else:
        dictmap[word[0:2]]=i
print(dictmap)
