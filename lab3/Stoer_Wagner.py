'''
Program obliczający spójność krawędziową grafu nieskierowanego G przy użyciu algorytmu Stoera-Wagnera.

[https://faliszew.github.io/algograf/lab3]

'''

from dimacs import loadWeightedGraph
from queue import PriorityQueue




def printG(G):
  
  for idx in range(1, len(G)):
    print(idx, end = " ")
  
    for (v,w) in G[idx].items():
      print((v,w), end = " ")
    print()
  print()


def merge(G,x,y):

  # usuwamy krawędzie z wierzchołka y i dodajemy do x
  # (wystarczy usunąć krawędź wchodzące do y, wychodzące niekoniecznie, 
  # bo i tak do tego wierzchołka nie da się już wejść)
  for (v,w) in G[y].items():

    if x in G[v] and v in G[x]:

      G[x][v] += w 
      G[v][x] =  G[x][v]
      del G[v][y]

    elif x != v :

      G[x][v] = G[v][x] = w
      del G[v][y]

    elif x == v:
      del G[v][y]
   
  

def minimumCutPhase(G,deleted):
  # zaczynamy od dowolnego wierzchołka, który tworzy zbiór jednoelementowy,
  # w kolejnych krokach dodając do niego taki wierzchołek, którego suma krawędzi 
  # łączących go z wierzchołkami tego zbioru jest największa

  # s i t to odpowiednio wierzchołki ostanio i przedostatnio dodane do zbioru S

  s = 1
  t = None

  # dla każdego v przechowuję aktualnie max sumę krawędzi łączących go z S
  current_sum = [0]*len(G)

  # do kolejki na początek wkładam tylko wierzchołek s i jego sąsiadów 
  PQ = PriorityQueue()

  PQ.put((0,1))
  for (v,w) in G[1].items():
    # (suma krawędzi do S, v)
    PQ.put((-1*w,v))
  

  visited = [False]*len(G)
  visited[0] = True
  visited[1] = True

  # licznik  pilnujący, by w zbiorze S znalazły się wszystkie wierzchołki
  ctr = 0
  
  while ctr != len(G)-2-deleted :

    (_, v) = PQ.get()

    if not visited[v]:

      t = s 
      s = v      
      for u, weight in G[v].items():
        current_sum[u] += weight
        PQ.put((-1*current_sum[u], u))
      
      visited[v] = True
      ctr += 1



  # zapamiętujemy sumę wag krawędzi wychodzących z s jako potencjalny wynik
  pot_res = 0

  for _, weight in G[s].items():
    pot_res += weight

  merge(G,s,t)
  #print("current size:", len(G) - 1 - deleted)
  deleted += 1


  return pot_res, deleted
  

def edge_connectivity(graph):

  (_,V,L) = loadWeightedGraph(graph)

  # wykorzystujemy słownik mapujący wierzchołki do których są krawędzie na ich wagi
  G = [{} for i in range(V+1)]
  
  for u, v, c in L: G[u][v] = G[v][u] = c

  deleted = 0


  result = float("inf")

  while deleted != len(G)-2:
    res, deleted = minimumCutPhase(G,deleted)
    result = min(result, res)

  return result
