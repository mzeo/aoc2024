cpu = {x+y*1j:col for y,row in enumerate(open(0)) for x,col in enumerate(row)}

start = next(p for p,i in cpu.items() if i=="S")
end = next(p for p,i in cpu.items() if i=="E")

search = {start}
path = {}
count = 0

while search:
    path |= {s:count for s in search}
    search = {q for s in search for d in range(4) if (q:=s+1j**d) not in path and cpu[q]!="#"}
    count += 1

path_list = [*zip(*sorted((d,p) for p,d in path.items()))][1]
assert start == path_list[0]
assert end == path_list[-1]
assert len(path_list) == len(path)

p2 = p1 = 0
track = set()

p = start
for x in range(-20,21):
    for y in range(-20,21):
        dist = abs(x)+abs(y)
        if dist <= 20:
            gain = path.get(p+x+1j*y,0)-path[p]-dist
            if gain >= 100:
                track |= {p+x+1j*y}

manhattan=lambda p:abs(p.imag)+abs(p.real)

for p in path_list:
    for d in range(4):
        if path.get(p++1j**d*2,0)-path[p]-2>=100:
            p1 += 1
    for x in range(-20,21):
        y = 20 - abs(x)
        track |= {p+x+1j*y, p+x-1j*y}
    track = {q for q in track if (dist:=manhattan(q-p))<=20 and path.get(q, 0)-path[p]-dist>=100}
    p2 += len(track)
print(p1, p2)
