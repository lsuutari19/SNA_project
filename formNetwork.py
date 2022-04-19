import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import statistics
from itertools import chain
import pandas as pd

"""
TO DO:
    - Debugging
    - checking that the values are correct (can be done by reducing sheet.nrows = 5 and manually calculating
        - for example the average centralities are currently done wrong
    - save in a file all the centralities and draw the degree distributions (instructions 3-5)

"""


file = "./databases/NEC.xls"

G = nx.Graph()

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(1)

# columns are 6 and 10, 14 for actor2 and actor1 and actor 3 respectively    (change 3 --> sheet.nrows when this works :D)
for row in range(1, sheet.nrows):
    data = sheet.row_slice(row)
    actor1 = data[6].value
    actor2 = data[10].value
    actor3 = data[14].value
    G.add_edges_from([(actor1, actor2), (actor1, actor3)])
    G.add_edges_from([(actor2, actor3)])


#draws the BIG CHUNGUS graph
#nx.draw(G, with_labels=True)
#plt.show()

print("Hello World!")


#writing the wanted information into results.txt
with open('results.txt', 'w') as f:
    """
    #numb of nodes in G
    f.write("number of nodes: " + str(G.number_of_nodes()) + "\n")

    #numb of edges
    f.write("number of edges: " + str(G.number_of_edges()) + "\n")

    #clustering coefficient
    f.write("clustering coefficient: " + str(nx.average_clustering(G)) + "\n")

    #diameter
    diameter = max([max(j.values()) for (i,j) in nx.shortest_path_length(G)])
    f.write("diameter: " + str(diameter) + "\n")

    #numb of components
    f.write("number of components: " + str(nx.number_connected_components(G)) + "\n")

    #largest component  
    #f.write("largest component: " + str(max(nx.connected_components(G), key=len)) + "\n")

    #avg path length
    path_lengths = (j.values() for (i,j) in nx.shortest_path_length(G))
    avg_path_len = statistics.mean(chain.from_iterable(path_lengths))
    f.write("avg path length: " + str(avg_path_len) + "\n")

    """
    #degree centralities in order of max, avg, min
    degr_cent = nx.degree_centrality(G)
    f.write("maximum degree centrality: " + str(min(degr_cent)) + " " + str(degr_cent.get(min(degr_cent))) + "\n")

    avg_degr_cent = sum(degr_cent.values()) / len(degr_cent)
    f.write("average degree centrality: " + str(avg_degr_cent) + "\n")

    f.write("minimum degree centrality: " + str(max(degr_cent)) + " " + str(degr_cent.get(max(degr_cent))) + "\n\n")

    #eigenvector centralities in order of max, avg, min
    eigvec_cent = nx.eigenvector_centrality(G)
    f.write("maximum eigenvector centrality: " + str(min(eigvec_cent)) + " " + str(eigvec_cent.get(min(eigvec_cent))) + "\n")

    avg_eigvec_cent = sum(eigvec_cent.values()) / len(eigvec_cent)
    f.write("average eigenvector centrality: " + str(avg_eigvec_cent) + "\n")

    f.write("minimum eigenvector centrality: " + str(max(eigvec_cent)) + " " + str(eigvec_cent.get(max(eigvec_cent))) + "\n\n")
    
    #betweenness centralities in order of max, avg, min
    betw_cent = nx.betweenness_centrality(G)
    f.write("maximum betweenness centrality: " + str(min(betw_cent)) + " " + str(betw_cent.get(min(betw_cent))) + "\n")

    avg_betw_cent = sum(betw_cent.values()) / len(betw_cent)
    f.write("average betweenness centrality: " + str(avg_betw_cent) + "\n")

    f.write("minimum betweenness centrality: " + str(max(betw_cent)) + " " + str(betw_cent.get(max(betw_cent))) + "\n\n")