graph = {}
for line in open(0):
    a, b = line.strip().split("-")
    graph[a] = graph.get(a, set()) | {b}
    graph[b] = graph.get(b, set()) | {a}
    assert a != b


def max_clique(remaining, current=set(), best=set()):
    if len(current) + len(remaining) <= len(best):
        return best
    best = max(current, best, key=len)
    while remaining:
        p = remaining.pop()
        best = max_clique(graph[p] & remaining, current | {p}, best)
    return best


clique3 = {
    tuple(sorted((n, i, j)))
    for n in graph
    if n[0] == "t"
    for i in graph[n]
    for j in graph[n] & graph[i]
}
print(len(clique3))
print(",".join(sorted(max_clique({*graph}))))
