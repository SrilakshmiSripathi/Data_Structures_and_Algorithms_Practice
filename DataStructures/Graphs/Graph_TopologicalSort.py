# Topological sort py 2.7v
import MyGraph
import heapq as hq


class DAG():

    def __init__(self, Graph):
        """ DAG Constructor; uses graphs adjList"""
        self.G = Graph
        self.TopOrder = []
        self.indegree = {}
        self.neighbors = {}
        self.pq = []

    def Initialize(self):
        """ To perform this sort we need to keep track of indegree,
            store neighbors and an empty priority queue with
            indegree as key and vertex and neighbors as values"""
        UniqVert = {}
        for vx in self.G:
            for v in vx:
                UniqVert.update({v: 0})

        self.indegree = UniqVert 
        for vx in self.G:
            self.indegree[vx[1]] = self.indegree.get(vx[1], 0) + 1
        print ("Given graphs indegrees", self.indegree)

        for vx in self.G:
            if vx[0] not in self.neighbors or vx[1] not in self.neighbors:
                self.neighbors[vx[0]] = [vx[1]]
                self.neighbors[vx[1]] = []
            else:
                self.neighbors[vx[0]].append(vx[1])

        for u in list(UniqVert):
            try:
                hq.heappush(self.pq, [self.indegree[u], u, self.neighbors[u]])
            except KeyError:
                hq.heappush(self.pq, [self.indegree[u], u, None])
        hq.heapify(self.pq)
        print ("PQ", self.pq)

    def TopologicalSort(self):

        """ Using Priority queue, we poll lowest indegree vertex;
            store the vertex to topological ordering list. Next we
            check this vertex neighbors indegree and we decrease
            it by one and update the Prioirty queue accordingly.
            Once Priority queue is empty we have the topological
            order saved in the list."""
        # Poll current lowest indegree vertex
        indegree, vertex, neighbors = hq.heappop(self.pq)
        # Store the polled vertex in toplogical order list
        self.TopOrder.append(vertex)
        # update all the neighbours indegree by decreasing by one
        if len(neighbors) != 0:
            for u in neighbors:
                self.indegree[u] = self.indegree[u] - 1
                for idx, pqval in enumerate(self.pq):
                    if pqval[1] == u:
                        self.pq[idx] =\
                                     [self.indegree[u], u, self.neighbors[u]]
            hq.heapify(self.pq)
            # Update PQ and return
            print ('PQ updated', self.pq)
        else:
            return

    def Print(self):
        print ("Topological Ordering Of Vertices",\
              "-->".join(map(str, self.TopOrder)))


def main(grFile):

    """ Main function generates a graph from .gr file
        using MyGraph class, once we have graph it initializes
        a priority queue, and does Topsort with the help
        of priority queue. Finally, prints the topsort
        order of the given graph """

    # Create Graph Object
    newGraph = MyGraph.genGraph(grFile)
    print ("Graph", newGraph)
    print (newGraph)
    # Create DAG Object
    dag = DAG(newGraph)
    # Initialize elements required for Topological sort
    dag.Initialize()
    # Perform Topological sort
    w = True
    while w:
        try:
            dag.TopologicalSort()
        except IndexError:
            w = False
    # Print Topological order
    dag.Print()


def driver():

    """Driver function to read graph(gr) file"""
    with open('graph3.gr', 'r') as graph1:
        main(graph1)
    graph1.close
    with open('new.gr', 'r') as graph2:
        main(graph2)
    graph2.close
driver()
