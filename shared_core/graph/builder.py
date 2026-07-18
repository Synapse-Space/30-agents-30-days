class GraphBuilder:
    def __init__(self):
        self.nodes={}

    def register(self,name,node):
        self.nodes[name]=node 
        