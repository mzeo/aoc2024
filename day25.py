# 149
E=enumerate
L=[{x+y*1j for y,r in E(l)for x,col in E(r)if col=="#"} for l in open(0).read().split("\n\n")]
print(sum(not a&b for a in L for b in L)//2)
