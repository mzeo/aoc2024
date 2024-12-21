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

def min_path(keypad, a, b, level):
    stride = keypad.find("\n")+1
    keya = keypad.find(a)
    keyb = keypad.find(b)
    dx = keyb%stride-keya%stride
    dy = keyb//stride-keya//stride

    result = []
    if keypad[keyb-dx]!=" ":
        result += [sequence_length("^v"[dy>0]*abs(dy)+"<>"[dx>0]*abs(dx)+"A",level-1)]
    if keypad[keya+dx]!=" ":
        result += [sequence_length("<>"[dx>0]*abs(dx)+"^v"[dy>0]*abs(dy)+"A",level-1)]

    return min(result)

@cache
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
