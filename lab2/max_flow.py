'''Dany jest graf skierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wierzchołki s i t. 
Należy znaleźć maksymalny przepływ w grafie G pomiędzy s i t, tzn. funkcję f: E -> N spełniającą warunki definicji 
przepływu, zapewniającą największą przepustowość.

Wierzchołek s ma nr 1, t nr V.

[https://faliszew.github.io/algograf/lab2]
'''

from dimacs import loadDirectedWeightedGraph

def build_graph(V,L):

  g = [[0]*V for _ in range(V)]

  for edge in L:
    x = edge[0]
    y = edge[1]
    w = edge[2]
    g[x-1][y-1] = w
  
  return g
  

from collections import deque

def BFS(g,s,t,parents):  
    
    q=deque()
    number=len(g)

    visited=[False]*number
    q.appendleft(s)  
    visited[s]=True

    while(len(q)!=0):
        u=q.pop()
        
        for i in range(number):
            if len(q) == 0 : q=deque()
            if(g[u][i]!=0 and visited[i]==False) :  
                parents[i]=u
                visited[i]=True
                q.appendleft(i)
    
                
    return visited[t]



def Ford_Fulkerson(graph):
  (V,L) = loadDirectedWeightedGraph(graph)
  g = build_graph(V,L)
  parents=[None]*V

  # aktualny przepływ w grafie
  flow = 0
  
  # powtarzam dopóki istnieje ścieżka z s do t
  while BFS(g,0,len(g)-1,parents):
    # szukamy najmniejszej pojemności na danej ścieżce
    # idziemy od t w górę po tablicy parentów

    current = len(g)-1
    current_flow = float("inf")
    
    while (current != 0):
      current_flow = min(current_flow, g[parents[current]][current])
      current = parents[current]

    flow += current_flow

    # aktualizujemy pojemności krawędzi i krawędzi powrotnych

    v = len(g)-1
    while (v != 0):
      g[parents[v]][v] -= current_flow
      g[v][parents[v]] += current_flow
      v = parents[v]

    for i in range(len(parents)):
      parents[i] = None
  
  print(flow)
  return flow
