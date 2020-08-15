## greedily select a remaining edge with the smallest weight which does not form a cycle.

parent = dict()

def make_set(vertice):
    parent[vertice] = vertice

# returns first element of set
def find_set(vertice):
    if parent[vertice] != vertice:
        return find_set(parent[vertice])
    else:
        return parent[vertice]


# joins two sets: set 1, which includes 'vertice1' and set 2, which includes 'vertice2'

def union(u, v, edges):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)

    # if u and v are not connected by a path
    if ancestor1 != ancestor2:
            parent[ancestor1] = ancestor2


def kruskal(graph):
    mst = set()
    # puts all the vertices in seperate sets
    for vertice in graph['V']:
        make_set(vertice)

    edges = list(graph['E'])
    # sorts edges in ascending order
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        
        # checks if current edge do not close cycle
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v, edges)
# mst is a set of selected edges
    return mst


# input graph
graph = {
        'V': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'E': set([
            (2, '1', '2'),       # weight, one node, another node
            (2, '1', '3'),
            (2, '2', '3'),
            (1, '2', '6'),
            (1, '3', '4'),
            (5, '4', '6'),
            (4, '6', '7'),
            (7, '4', '5'),
            (6, '7', '5'),
            (1, '4', '10'),
            (2, '5', '10'),
            (8, '5', '8'),
            (2, '5', '9'),
            (3, '8', '9'),
            ])
        }


mst = kruskal(graph)
print("Minimal Spanning Tree:")
print(mst)
mst_weight = 0
for edge in mst:
    weight, u, v = edge
    mst_weight += weight

print("Cost: ")
print(mst_weight)
