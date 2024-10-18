import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import lines

def simple_visualization(data,mazeStructure):
  print(mazeStructure)
  G = nx.Graph(data.g)
  plt.figure(figsize=(20, 15))
  plt.title('Maze graph')
  nodes_colors=[]
  for node in data.graph_dict.keys():
    #print (node)
    #print (mazeStructure[node[0],node[1]])
    if mazeStructure[node[0],node[1]]==0:
      nodes_colors.append('red')
    else:
      nodes_colors.append('blue')
  edge_weights = {(k, v2) : k2 for k, v in data.graph_dict.items() for k2, v2 in v.items()}#actions
  pos = nx.spring_layout(G)
  nx.draw_networkx_nodes(G,pos,linewidths=0.3, node_color= nodes_colors, node_size=200)
  nx.draw_networkx_edges(G,pos)
  nx.draw_networkx_labels(G,pos,font_size=8)
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weights,font_size=8)


def simple_visualization1(data,mazeStructure):
  print(mazeStructure)
  G = nx.Graph(data.g)
  print(len(G.nodes))
  print(G.nodes)
  plt.figure(figsize=(20, 15))
  plt.title('Maze graph')
  nodes_colors=['blue' for node in G.nodes]
  edge_weights={}

  for k, v in data.graph_dict.items():
    if len(v) != 0:
      for k2, v2 in v.items():
        edge_weights.setdefault((k, v2), k2)
  print(len(edge_weights), len (nodes_colors))



  #edge_weights = {(k, v2) : k2 for k, v in data.graph_dict.items() for k2, v2 in v.items()}#actions
  pos = nx.spring_layout(G)
  nx.draw_networkx_nodes(G,pos,linewidths=0.3, node_color= nodes_colors, node_size=200)
  nx.draw_networkx_edges(G,pos)
  nx.draw_networkx_labels(G,pos,font_size=8)
  nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weights,font_size=8)
  


def drawSearchTree(gData, mazeStructure,nodeColors):
  print(mazeStructure)
  G = nx.Graph(gData.g)
  plt.figure(figsize=(20, 15))
  plt.title('Maze solution graph')
  nodes_colors=[]
  print(nodeColors)
  for node in gData.graph_dict.keys():
    #print (node)
    #print (mazeStructure[node[0],node[1]])
    if mazeStructure[node[0],node[1]]==0:
      nodes_colors.append('red')
    else:
      if node in nodeColors.keys():
        nodes_colors.append(nodeColors[node])
      else:
        nodes_colors.append('grey')
  print(nodeColors)
  #node_label_pos = {k:[v[0],v[1]-0.5]  for k,v in gData.locations.items()}

  pos = nx.spring_layout(G)
  print(len(G.nodes), len(nodes_colors))
  nx.draw_networkx_nodes(G,pos,linewidths=0.3, node_color=nodes_colors,
                     node_size=200)
  nx.draw_networkx_edges(G,pos)
  nx.draw_networkx_labels(G,pos,font_size=8)
  #nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weights,font_size=8)

  # draw the graph (both nodes and edges) with locations
  #nx.draw(G, pos={k: gData.locations[k] for k in G.nodes()},node_color=[nodeColors[node] for node in gData.g.keys()], linewidths=0.3, edgecolors='k', node_size=100)
      
  # draw labels for nodes
  #node_label_handles = nx.draw_networkx_labels(G, pos=node_label_pos, font_size=8)
  
  # add edge lables to the graph
  #nx.draw_networkx_edge_labels(G, pos=gData.locations, edge_labels=edge_weights, font_size=8, font_color='r')
  # displaying the title
  #plt.title('Search graph')
  # add a legend
  white_circle = lines.Line2D([], [], color="white", marker='o', markersize=10, markerfacecolor="white")
  orange_circle = lines.Line2D([], [], color="orange", marker='o', markersize=10, markerfacecolor="orange")
  red_circle = lines.Line2D([], [], color="red", marker='o', markersize=10, markerfacecolor="red")
  blue_circle = lines.Line2D([], [], color="blue", marker='o', markersize=10, markerfacecolor="blue")
  green_circle = lines.Line2D([], [], color="green", marker='o', markersize=10, markerfacecolor="green")
  plt.legend((white_circle, orange_circle, red_circle, blue_circle, green_circle),
               ('Un-explored', 'Frontier', 'Currently Exploring', 'Explored', 'Final Solution'),
               numpoints=1, prop={'size': 8}, loc=(1.25, .95))
  plt.show()

