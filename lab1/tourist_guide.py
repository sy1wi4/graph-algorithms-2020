'''
Dany jest graf nieskierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wierzchołki s i t. 
Należy znaleźć scieżkę z s do t taką, że najmniejsza waga krawędzi na tej ścieżce jest jak największa.

Wierzchołek s ma nr 1, t nr 2.

[https://faliszew.github.io/algograf/lab1]
'''

# ALGORYTM:
'''
Wykorzystujemy strukturę find union, by po posortowaniu krawędzi malejąco po wagach, móc brać kolejne krawędzi, łącząc sety,
do których należą wierzchołki połączone tą krawędzią (union). Dzięki temu, gdy s i t znajdą się w jednym zbiorze kończymy 
algorytm - rozwiązaniem problemu jest waga ostatnio wziętej krawędzi.
'''

from dimacs import loadWeightedGraph


# FIND UNION

class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self      
        self.rank=0        


def find_set(x) :
    if x != x.parent :
      
        x.parent=find_set(x.parent)
    return x.parent 


def union(x,y):
    x=find_set(x)
    y=find_set(y)

    if x.rank > y.rank :
        y.parent=x
        
    elif y.rank > x.rank:
        x.parent=y

    else :
        x.parent=y
        y.rank+=1 




# wczytuje graf i wypisuje krawędzi

(V,L) = loadWeightedGraph( "g1" )        # wczytaj graf
for (x,y,c) in L:                        # przeglądaj krawędzie z listy
  print( "krawedz miedzy", x, "i", y,"o wadze", c )   # wypisuj
print()




def tour(graph):

    # V - liczba wierzchołków, L - lista krawędzi postaci(x,y,weight)
    (V,L) = loadWeightedGraph(graph) 


        
    # sortowanie krawędzi grafu malejąco - sortuję krotki po wadze
    L.sort(key=lambda tup: tup[2], reverse = True)

    nodes = [Node(i+1) for i in range(V)]
    
   
    for x,y,weight in L:

        if find_set(nodes[x-1]) != find_set(nodes[y-1]):
            union(nodes[x-1],find_set(nodes[y-1]))
        
        # koniec algorytmu
        if find_set(nodes[0]) == find_set(nodes[1]):
            return weight
