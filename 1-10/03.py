tar="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

tar=tar.replace(",","").replace("'","").replace(".","")
target=tar.split(" ")

num=[]

for i in target:
    num.append(len(i))

print(num)
