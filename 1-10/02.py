tar1="パトカー"
tar2="タクシー"

tar=""
for i,j in zip(tar1,tar2):
    tar+=i
    tar+=j
print(tar)
