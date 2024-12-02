INF = 999
class GraphNode:
    def __init__(self, key, hCost):
        self.id = key
        self.hCost = hCost
        self.gCost = INF
        self.fCost = self.hCost
        self.adjNode = {}
        self.preId = None

    def getNode(self):
        return self.id

    def getPreNode(self):
        return self.preId

    def addAdjNode(self, nbr, weight=0):
        if nbr not in self.adjNode.keys():
            self.adjNode[nbr] = weight

    def getAdjNode(self):
        return self.adjNode.keys()

    def getWeight(self, nbr):
        return self.adjNode[nbr]

    def getGCost(self):
        return self.gCost

    def getFCost(self):
        return self.fCost

    def refreshPreNode(self, preId):
        self.preId = preId

    # 访问邻居节点
    def getNeighbor(self):
        nbr = list()
        for id in self.adjNode.keys():
            nbr.append(id)
        return nbr

    def getHCost(self):
        return self.hCost

    def refreshFCost(self):
        #self.fCost = self.gCost + self.hCost
        self.fCost =self.hCost
        return self.fCost

    def refreshGCost(self, GCost):
        self.gCost = GCost

class Graph:
    def __init__(self):
        self.nodeList = {}
        self.nodeNum = 0

    def addNode(self, key, hCost=INF):
        if key not in self.nodeList:
            self.nodeList[key] = GraphNode(key, hCost)
            self.nodeNum += 1

    def addEdge(self, key_1, key_2, weight):
        if key_1 not in self.nodeList:
            self.addNode(key_1)
        if key_2 not in self.nodeList:
            self.addNode(key_2)
        self.nodeList[key_1].addAdjNode(key_2, weight)
        self.nodeList[key_2].addAdjNode(key_1, weight)

    def searchGraph(self, start_id, goal_id):
        open_list = [start_id]
        closed_list = set()
        start = self.nodeList[start_id]
        start.refreshGCost(0)
        start.refreshFCost()

        while open_list:
            current_node_id = min(open_list, key=lambda node_id: self.nodeList[node_id].getFCost())
            current_node = self.nodeList[current_node_id]
            open_list.remove(current_node_id)
            closed_list.add(current_node_id)

            if current_node_id == goal_id:
                return self.reconstructPath(goal_id, start_id), closed_list, neighbor_cost

            for neighbor_id in current_node.getNeighbor():
                neighbor = self.nodeList[neighbor_id]
                if neighbor not in closed_list:
                    neighbor_cost = current_node.getGCost() + current_node.getWeight(neighbor_id)

                    if neighbor_cost < neighbor.getGCost():
                        neighbor.refreshPreNode(current_node_id)
                        neighbor.refreshGCost(neighbor_cost)
                        neighbor.refreshFCost()

                        if neighbor not in open_list:
                            open_list.append(neighbor_id)

        # 如果未找到路径，返回None
        return None


    def reconstructPath(self, current_node_id, start_id):
        path = []
        while current_node_id != start_id:
            path.append(current_node_id)
            current_node = self.nodeList[current_node_id]
            current_node_id = current_node.preId
        path.append(start_id)
        path.reverse()
        return path

dataHCost = {
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

dataEdge = {
    'Oradea-Zerind': 71,
    'Oradea-Sibiu': 151,
    'Arad-Timisoara': 118,
    'Arad-Sibiu': 140,
    'Arad-Zerind': 75,
    'Timisoara-Lugoj': 111,
    'Lugoj-Mehadia': 70,
    'Mehadia-Drobeta': 75,
    'Drobeta-Craiova': 120,
    'Drobeta-Mehadia': 75,
    'Sibiu-Fagaras': 99,
    'Sibiu-Rimnicu Vilcea': 80,
    'Sibiu-Arad': 140,
    'Sibiu-Oradea': 151,
    'Craiova-Rimnicu Vilcea': 146,
    'Craiova-Pitesti': 138,
    'Pitesti-Rimnicu Vilcea': 97,
    'Fagaras-Bucharest': 211,
    'Bucharest-Giurgiu': 90,
    'Bucharest-Pitesti': 101,
    'Rimnicu Vilcea-Sibiu': 80,
    'Rimnicu Vilcea-Pitesti': 97
}

def initGraph(dataHCost,dataEdge):
    graph = Graph()

    for key in dataHCost.keys():
        graph.addNode(key, dataHCost[key])

    for key in dataEdge.keys():
        key_1, key_2 = key.split("-")
        graph.addEdge(key_1, key_2, dataEdge[key])
        # print(graph.getEdge(key_2, key_1))
    return graph


g = initGraph(dataHCost, dataEdge)
Optimal_Path, closed_list, Path_len = g.searchGraph("Oradea", "Bucharest")
print('Optimal Path:',Optimal_Path,'\nReachedNode:', closed_list,'\nPath Length:', Path_len)

