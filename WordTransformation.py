# https://vjudge.net/problem/UVA-429
# andrekuru's solution for [UVA-429] [Problem A]

words = []
dictionary = {}
steps = {}
visited = set()

def get_neighbour(word):
    if word in dictionary:
        return dictionary[word]
    
    neigbours = []
    for w in words:
        if len(word) == len(w):
            mismatch = 0
            for c1, c2 in zip(word, w):
                if c1 != c2:
                    mismatch += 1
                    if mismatch > 1: break
                
            if mismatch == 1:
                neigbours.append(w)

    dictionary[word] = neigbours
    return neigbours

def bfs(s, e):
    visited.clear()
    steps.clear()

    queue = [s]
    visited.add(s)
    steps[s] = 0
    while queue:
        w = queue.pop(0)
        cur_step = steps[w]
        for neighbour in get_neighbour(w):
            if neighbour == e: return cur_step + 1
            if neighbour not in visited:
                visited.add(neighbour)
                steps[neighbour] = cur_step + 1
                queue.append(neighbour)


N = int(input())
input()

for i in range(N):

    if i > 0: print("")

    words.clear()
    dictionary.clear()

    word = input()
    while(word != '*'):
        words.append(word)
        word = input()

    # print(words)

    while True:
        try:
            start, end = input().split()
            print(f"{start} {end} {bfs(start, end)}")
        # print(dictionary)
        # print(start, end)
        except ValueError: break
        except EOFError: break
    

'''
1

dip
lip
mad
map
maple
may
pad
pip
pod
pop
sap
sip
slice
slick
spice
stick
stock
*
spice stock
may pod
'''