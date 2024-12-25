# 95
L=[*open(0).read().split("\n\n")]
print(sum(("#","#")not in zip(a,b)for a in L for b in L)//2)
