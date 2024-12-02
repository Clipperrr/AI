graph = [[0]*5 for _ in range(5)]
graph[0][1] = 1
def diagonal_check(i, j):
    m, n = i, j
    while i < 4 and j < 4:
        i += 1
        j += 1
        if graph[i][j] == 1:
            return False
    i, j = m, n
    while i < 4 and j > 0:
        i += 1
        j -= 1
        if graph[i][j] == 1:
            return False
    i, j = m, n
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if graph[i][j] == 1:
            return False
    i, j = m, n
    while i > 0 and j < 4:
        i -= 1
        j += 1
        if graph[i][j] == 1:
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
    for j in range(0, 5):
        if valid_check(cnt, j):
            graph[cnt][j] = 1
            cnt += 1
            if backtrack(cnt):
                return True
            else:
                cnt -= 1
                graph[cnt][j] = 0
    return False

if backtrack(1):
    for i in graph:
        print(i)
else:
    print("No Solutions Found")