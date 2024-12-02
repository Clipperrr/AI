graph = {
    'Arad': 366,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'lasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374,
    'Bucharest': 0
}
route = {
    'Oradea': [{'Zerind': 71}, {'Sibiu': 151}],
    'Zerind': [{'Arad': 75}, {'Oradea': 71}],
    'Arad': [{'Timisoara': 118}, {'Sibiu': 140}, {'Zerind': 75}],
    'Timisoara': [{'Lugoj': 111}, {'Arad': 118}],
    'Lugoj': [{'Mehadia': 70}, {'Timisoara': 111}],
    'Mehadia': [{'Drobeta': 75}, {'Lugoj': 70}],
    'Drobeta': [{'Craiova': 120}, {'Mehadia': 75}],
    'Sibiu': [{'Fagaras': 99}, {'Rimnicu Vilcea': 80}, {'Arad': 140}, {'Oradea': 151}],
    'Craiova': [{'Rimnicu Vilcea': 146}, {'Pitesti': 138}, {'Drobeta': 120}],
    'Pitesti': [{'Rimnicu Vilcea': 97}, {'Craiova': 138}, {'Bucharest': 101}],
    'Fagaras': [{'Sibiu': 99}, {'Bucharest': 211}],
    'Bucharest': [{'Fagars': 211}, {'Giurgiu': 90}, {'Pitesti': 101}],
    'Giurgiu': [{'Bucharest': 90}],
    'Rimnicu Vilcea': [{'Sibiu': 80}, {'Craiova': 146}, {'Pitesti': 97}]
}

Start = 'Oradea'
visited = []
stack = [Start]
path = []
current = Start

while stack:
    current = stack[-1]
    if current == 'Bucharest':
        path.append(current)
        break
    child = []
    sub_dict = {}
    for i in route[current]:
        child.append(list(i.keys()).pop())
    for j in child:
        sub_dict[j] = graph[j]
    sub_dict_ordered = sorted(sub_dict.items(), key=lambda kv: [kv[1]], reverse=True)
    sub_stack = [row[0] for row in sub_dict_ordered]

    #print(sub_stack)
    if current not in visited:  # 如果该节点未被访问过
        path.append(current)
        visited.append(current)  # 标记为已访问

        if current in graph:
            stack.extend(i for i in sub_stack if i not in visited)      #Under the order of the origin
            #print(stack)
        else:
            stack.pop()
            path.pop()
    else:
        stack.pop()
        if current in path:
            path = path[0:path.index(current)]

print("final_path: ", path)