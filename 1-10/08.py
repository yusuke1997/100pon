
def cipher(moji):
    res=""
    for i in moji:
        if(i.islower()):
            res+=chr(219-ord(i))
        else:
            res+=i
    return res

res=cipher("frewghyjkujyhtewertyjukig\\5jO4")
print("encrypt is",res)
res2=cipher(res)
print("decrypt is",cipher(res))
