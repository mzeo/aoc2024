#277 chars
C=[*open(0).read()]
S=C.index("\n")+1
p=[]
n=[C.index("S")]
p1=p2=0
while n:
 g=1
 for q in p[::-1]:
  x,y=n[0]%S,n[0]//S;u,v=q%S,q//S;d=abs(x-u)+abs(y-v)
  if g-d>=100:p1+=d<=2;p2+=d<=20
  g+=1
 p+=n;n=[q for d in(-1,1,-S,S)if C[q:=p[-1]+d]!="#"and[q]!=p[-2:-1]]
print(p1,p2)
