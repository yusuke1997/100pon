
def templete(X,Y,Z):
    string="{X}時の{Y}は{Z}".format(X=X,Y=Y,Z=Z)

    return string


X=12
Y="気温"
Z=22.4

print(templete(X,Y,Z))
