
def dn(n):
    n = n+sum(map(int,str(n)))
    return n

notself = set()

for i in range(1, 10001):
    notself.add(dn(i))
for j in range(1, 10001):
    if j not in notself:
        print(j)