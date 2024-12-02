graph = {
'S': ['p', 'e', 'd'],
'e': ['c', 'r', 'h'],
'p': ['q'],
'd': ['b'],
'b': ['a'],
'c': ['a'],
'r': ['f'],
'h': ['q', 'p'],
'f': ['G', 'c']
}

Start = 'S'
visited = []
stack = [Start]
path = []
while stack:
    current = stack[-1]
    if current not in visited:  # 如果该节点未被访问过
        path.append(current)
        visited.extend(current)  # 标记为已访问
        if current == 'G':
            break
        if current in graph:
            stack.extend(i for i in graph[current] if i not in visited)      #Under the order of the origin
            #stack.extend(set(graph[current]) - set(visited))                #Under the order of the Alphabet
        else:
            stack.pop()
            path.pop()
    else:
        stack.pop()
        if current in path:
            path = path[0:path.index(current)]
    print("step_path: ", path, "\n")
    print("step_stack", stack)

print("final_visited: ", visited)
print("final_path: ", path)