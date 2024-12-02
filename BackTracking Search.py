graph = {
    'A1': ['A2', 'H'],
    'A2': ['A1', 'A3', 'H'],
    'A3': ['A2', 'A4', 'H'],
    'A4': ['A3', 'H'],
    'H':  ['A1', 'A2', 'A3', 'A4', 'T'],
    'T':  ['H', 'F1', 'F2'],
    'F1': ['T'],
    'F2': ['T', 'K'],
    'K':  ['H', 'F2']
}

variable_order = ['A1', 'H', 'A4', 'F1', 'A2', 'F2', 'A3', 'T', 'K']
colors = ['R', 'G', 'B']
color_dict = {}

def valid_check(current, current_color):
    for neibors in graph[current]:
        if neibors in color_dict and color_dict[neibors] == current_color:
            return False
    return True

def backtrack(index):
    if index == len(variable_order):
        return True
    for color in colors:
        if valid_check(variable_order[index], color):
            color_dict[variable_order[index]] = color
            if backtrack(index + 1):
                return True
            else:
                del color_dict[variable_order[index]]
    return False

if backtrack(0):
    for node in graph:
        print("Node: ", node, "Color: ", color_dict[node])
else:
    print("No Solutions Found")
