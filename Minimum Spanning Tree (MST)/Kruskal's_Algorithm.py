## greedily select a remaining edge with the smallest weight which does not form a cycle.


def kruskal(graph):
    nodes = graph.keys()   ## ["s1" to "s5"]
    visited = set()        ## visited nodes; 
                           ## NOTE: it's a set (no duplicate nodes)
    path = []              ## printed path (not necessarily sequential)
    
    while len(visited) < len(nodes):
        distance = float('inf') 
        for s in nodes:
            for d in nodes:
                if s in visited and d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    one = s
                    two = d
        path.append((one, two))
        visited.add(one)
        visited.add(two)

    return path


if __name__ == '__main__':
    graph_dict = {"s1":{"s1": 0, "s2": 6, "s3": 3, "s4": 4, "s5":7},             ## should be symmetric
                    "s2":{"s1": 6, "s2": 0, "s3": 10, "s4": 8, "s5":9},
                    "s3":{"s1": 3, "s2": 10, "s3": 0, "s4":2, "s5":1},
                    "s4":{"s1": 4, "s2": 8, "s3": 2, "s4":0,"s5":11},
                    "s5":{"s1": 7, "s2": 9, "s3": 1, "s4":11,"s5":0},
    }
    path = kruskal(graph_dict)
    print(path)
