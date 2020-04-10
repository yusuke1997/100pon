from ngram import ngram

tar1="paraparaparadise"
tar2="paragraph"


result1=ngram.ngram(tar1,2)
result2=ngram.ngram(tar2,2)

res1=set(result1)
res2=set(result2)

union=res1|res2
product=res1&res2
diff=res1-res2

print(res1)
print(res2)
print(union)
print(product)
print(diff)

if "se" in res1:
    print("X includes se")
else:
    print("X doesn't include se")

if "se" in res2:
    print("Y includes se")
else:
    print("Y doesn't include se")
