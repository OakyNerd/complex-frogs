from graphClass import Graph

class myMap(Graph):
  def __init__(self, graph_dict=None, locations=None):
    super().__init__(graph_dict)
    self.locations=locations

  def getLocation(self,a):
    return self.locations.get(a)

