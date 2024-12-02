from collections import deque
graph = {
'S': ['d', 'e', 'p'],
'e': ['c', 'r', 'h'],
'p': ['q'],
'd': ['b','e'],
'b': ['a'],
'c': ['a'],
'r': ['f'],
'h': ['q', 'p'],
'f': ['c', 'G']
}

Start = 'S'
End = 'G'
visited = []
stack = deque()
stack.append(Start)
parent = {Start: None}
path = []
while stack:
    current = stack.popleft()
    if current == End:
        visited.extend(End)
        break
    if current in graph:
        for i in graph[current]:
            if i not in visited:
                stack.append(i)
                parent[i] = current

    visited.extend(current)
path = []
node = 'G'
while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()
#print(parent['e'])      #The order of the table influence the path.
print('Path: ', path)
print('Visited: ', visited)
