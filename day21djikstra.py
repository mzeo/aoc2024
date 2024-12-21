from functools import cache

numpad="""\
789
456
123
 0A
"""

arrows="""\
 ^A
<v>
"""

def dijkstra(start, end, edges, init=0, combine=int.__add__):
    import heapq

    search = [(init, start, None)]
    visited = {}
    while search:
        score, p, q = heapq.heappop(search)
        if p in visited:
            continue
        visited[p] = q
        if end == p:
            return score
        for w,q in edges(p):
            heapq.heappush(search,(combine(score,w),q,p))

@cache
def min_path(keypad, a, b, level):
    stride = keypad.find("\n")+1
    start = keypad.find(a)
    end = keypad.find(b)

    def edges(p):
        p, f = p
        # For all actions
        for d, k in (-1,"<"),(1,">"),(-stride,"^"),(stride,"v"),(0,"A"):
            q = p + d
            # Consider possible ones
            if 0 <= q < len(keypad) and keypad[q] not in " \n":
                yield (level == 0 or min_path(arrows,f or "A",k,level-1)), (q, k)

    return dijkstra((start, None), (end, "A"), edges)

def sequence_length(keys, level, keypad=arrows):
    if level<0:
        return len(keys)
    result = 0
    for a,b in zip("A"+keys, keys):
        result += min_path(keypad,a,b,level)
    return result

p2 = p1 = 0
for code in open(0):
    numeric = int(code[:-2])
    p1 += numeric * sequence_length(code[:-1],2,numpad)
    p2 += numeric * sequence_length(code[:-1],25,numpad)
print(p1, p2)
