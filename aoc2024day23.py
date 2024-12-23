lines = [*zip(*[l.strip().split("-") for l in open(0)])]

computers = {*(lines[0]+lines[1])}

edges = {}
for a,b in zip(lines[0],lines[1]):
    edges[a] = edges.get(a,set()) | {b}
    edges[b] = edges.get(b,set()) | {a}
    assert a!=b

def max_clique(current,remaining,minimum=0):
    if len(current)+len(remaining) <= minimum:
        return
    result = current if len(current) > minimum else None
    remaining = {*remaining}
    while remaining:
        p = remaining.pop()
        if current&edges[p]==current:
            clique = max_clique(current|{p},edges[p]&remaining,minimum)
            if len(clique or []) > minimum:
                minimum = len(clique)
                result = clique
    return result

clicks=set()
best=set()
for c in computers:
    clique = max_clique({c},edges[c],len(best))
    if len(clique or []) > len(best):
        best = clique

    if c[0]!="t":
        continue
    for i in edges[c]:
        for j in edges[c]&edges[i]:
            clicks |= {tuple(sorted((c,i,j)))}

print(len(clicks))
print(",".join(sorted(best)))
