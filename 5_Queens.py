graph = [[0]*5 for _ in range(5)]
graph[0][1] = 1
def diagonal_check(i, j):
    m, n = i, j
    while i < 5 and j < 5:
        if graph[i+1][j+1] == 1:
            return False
    i, j = m, n
    while i < 5 and j > 0:
        if graph[i+1][j-1] == 1:
            return False
    i, j = m, n
    while i > 0 and j > 0:
        if graph[i-1][j-1] == 1:
            return False
    i, j = m, n
    while i > 0 and j < 5:
        if graph[i-1][j+1] == 1:
            return False
    return True

def valid_check(i,j):
    for k in range(0, 5):
        if graph[i][k] == 1 or graph[k][j] == 1:
            return False
    if diagonal_check(i, j):
        return True
    return False

def backtrack(cnt):
    if cnt == 5:
        return True
    for i in range(cnt, 5):
        for j in range(0, 5):
            if valid_check(i, j):
                graph[i][j] = 1
            if backtrack(cnt + 1):
                print(graph)
                return True
            else:
                graph[i][j] = 0
    print(graph)
    return False

if backtrack(1):
    print(graph)
else:
    print("No Solutions Found")