from random import randint

graph = [[0] * 5 for _ in range(5)]
locates = {i: randint(0, 4) for i in range(5)}
for i in range(5):
    graph[i][locates[i]] = 1
def diagonal_check(i, j):
    cnt = 0
    m, n = i, j
    while i < 4 and j < 4:
        i += 1
        j += 1
        if graph[i][j] == 1:
            cnt += 1
    i, j = m, n
    while i < 4 and j > 0:
        i += 1
        j -= 1
        if graph[i][j] == 1:
            cnt += 1
    i, j = m, n
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if graph[i][j] == 1:
            cnt += 1
    i, j = m, n
    while i > 0 and j < 4:
        i -= 1
        j += 1
        if graph[i][j] == 1:
            cnt += 1
    return cnt

def valid_check(i,j):
    cnt = 0
    for k in range(0, 5):
        if graph[i][k] == 1 and k!=j:
            cnt += 1
        if graph[k][j] == 1 and k!=i:
            cnt += 1
    return cnt + diagonal_check(i, j)

def MinConflict(max_steps=1000):
    for _ in range(max_steps):
        conflict = [i for i in range(5) if valid_check(i, locates[i]) > 0]
        if not conflict:
            return True
        i = conflict[randint(0, len(conflict) - 1)]
        min_conflicts = 9
        min_locates = locates[i]
        for j in range(5):
            graph[i][locates[i]] = 0
            conflicts = valid_check(i, j)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_locates = j
        graph[i][min_locates] = 1
        locates[i] = min_locates
    return False

if MinConflict(100):
    for i in graph:
        print(i)
else:
    print("No Solutions Found")

