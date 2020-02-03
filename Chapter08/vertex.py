

class Vertex():

    def __init__(self, key):
        self.key = key
        # to keep the relationship with other vertex
        self.adj_vert = {}
        self.color = None
        self.distance = 0
        self.predecessor = None
        self.discovery = 0
        self.finish = 0

    def add_neighbor(self, nbr, weight=0):
        self.adj_vert[nbr] = weight

    def __str__(self):
        return str(self.key) + " connected to " + str([x.key for x in self.adj_vert])

    def get_connections(self):
        return self.adj_vert.keys()
    
    def get_key(self):
        return self.key

    def get_weight(self, nbr):
        return self.adj_vert.get(nbr)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def get_predecessor(self):
        return self.predecessor

    def set_predecessor(self, predecessor):
        self.predecessor = predecessor

    def get_discovery(self):
        return self.discovery

    def set_discovery(self, discovery):
        self.discovery = discovery

    def get_finish(self):
        return self.finish

    def set_finish(self, finish):
        self.finish = finish
        