# directed graph


from collections import defaultdict
from heapq import *

def dijkstra(edges, s, t):      #source node s and sink node t
    
    g = defaultdict(list)
    for l,r,edge_cost in edges:
        g[l].append((edge_cost,r))

    queue = [(0,s,())]     #priority queue  
    seen = set()           #processed nodes  
    mins = {s: 0}          #prev stored v and A[v]
    
    while queue:
        (A_v,v,path) = heappop(queue)                  #pop the node v with least cost A[v]
        seen.add(v)                                    #label this node as processed
        path = (v, path) 
        if v == t: return (A_v, path)                  #output the shortest distance and path

        for edge_cost, w in g.get(v, ()):           #get the neighbors of v from dict
            if w in seen: continue                  #ignore w if it has been processed
            prev = mins.get(w, None)
            next = A_v + edge_cost
            if prev is None or next < prev:         #update A[w] using Dijkstra's greedy criterion
                mins[w] = next
                heappush(queue, (next, w, path))
    return float("inf")
  
 edges = [
        ("s", "a", 1),
        ("s", "b", 4),
        ("a", "b", 2),
        ("a", "c", 6),
        ("b", "c", 3)
        ]

print("Dijkstra's shorest path from 's' to 'c' is")
print(dijkstra(edges, "s", "c"))


# output: Dijkstra's shorest path from 's' to 'c' is
#         (6, ('c', ('b', ('a', ('s', ())))))
