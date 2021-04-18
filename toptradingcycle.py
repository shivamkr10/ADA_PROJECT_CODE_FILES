from graph import *



def getpats(G, cycle, pats):

   if cycle.vertexId in pats:
      cycle = cycle.anyNext()

   startingHouse = cycle
   currentVertex = startingHouse.anyNext()
   thepats = set()

   while currentVertex not in thepats:
      thepats.add(currentVertex)
      currentVertex = currentVertex.anyNext()
      currentVertex = currentVertex.anyNext()

   return thepats


def anyCycle(G):
   visited = set()
   v = G.anyVertex()

   while v not in visited:
      visited.add(v)
      v = v.anyNext()

   return v



def topTradingCycles(pats, dons, agentPreferences, initialOwnership):
   pats = set(pats)
   vertexSet = set(pats) | set(dons)
   G = Graph(vertexSet)

   currentPreferenceIndex = dict((a,0) for a in pats)
   preferredHouse = lambda a: agentPreferences[a][currentPreferenceIndex[a]]

   for a in pats:
      G.addEdge(a, preferredHouse(a))
   for h in dons:
      G.addEdge(h, initialOwnership[h])

   allocation = dict()
   while len(G.vertices) > 0:
      cycle = anyCycle(G)
      cyclepats = getpats(G, cycle, pats)

      for a in cyclepats:
         h = a.anyNext().vertexId
         allocation[a.vertexId] = h
         G.delete(a)
         G.delete(h)

      for a in pats:
         if a in G.vertices and G[a].outdegree() == 0:
            while preferredHouse(a) not in G.vertices:
               currentPreferenceIndex[a] += 1
            G.addEdge(a, preferredHouse(a))
   print(allocation)
   return allocation

