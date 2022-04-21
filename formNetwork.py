from ctypes import sizeof
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import statistics
from itertools import chain
import pandas as pd
import numpy as np

"""
TO DO:
    - Debugging
    - checking that the values are correct (can be done by reducing sheet.nrows = 5 and manually calculating
        - for example the degree centrality max is smaller than min?
    - save in a file all the centralities and draw the degree distributions (instructions 3-5)

"""


file = "./databases/NEC.xls"

G = nx.Graph()

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(1)


# columns are 6 and 10, 14 for actor2 and actor1 and actor 3 respectively
for row in range(1, sheet.nrows):
    data = sheet.row_slice(row)
    actor1 = data[6].value
    actor2 = data[10].value
    actor3 = data[14].value
    G.add_edges_from([(actor1, actor2), (actor1, actor3)])
    G.add_edges_from([(actor2, actor3)])

#print(nx.info(G))

#draws the BIG CHUNGUS graph
#nx.draw(G, with_labels=True)
#plt.show()

print("Starting calculations!")


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

    degr_cent = nx.degree_centrality(G)
    eigvec_cent = nx.eigenvector_centrality(G)
    betw_cent = nx.betweenness_centrality(G)
    """
    #degree centralities in order of max, avg, min
    f.write("maximum degree centrality: " + str(min(degr_cent)) + " " + str(degr_cent.get(min(degr_cent))) + "\n")
    avg_degr_cent = sum(degr_cent.values()) / len(degr_cent)
    f.write("average degree centrality: " + str(avg_degr_cent) + "\n")
    f.write("minimum degree centrality: " + str(max(degr_cent)) + " " + str(degr_cent.get(max(degr_cent))) + "\n\n")

    #eigenvector centralities in order of max, avg, min
    f.write("maximum eigenvector centrality: " + str(max(eigvec_cent)) + " " + str(eigvec_cent.get(max(eigvec_cent))) + "\n")
    avg_eigvec_cent = sum(eigvec_cent.values()) / len(eigvec_cent)
    f.write("average eigenvector centrality: " + str(avg_eigvec_cent) + "\n")
    f.write("minimum eigenvector centrality: " + str(min(eigvec_cent)) + " " + str(eigvec_cent.get(min(eigvec_cent))) + "\n\n")
    
    #betweenness centralities in order of max, avg, min
    f.write("maximum betweenness centrality: " + str(max(betw_cent)) + " " + str(betw_cent.get(max(betw_cent))) + "\n")
    avg_betw_cent = sum(betw_cent.values()) / len(betw_cent)
    f.write("average betweenness centrality: " + str(avg_betw_cent) + "\n")
    f.write("minimum betweenness centrality: " + str(min(betw_cent)) + " " + str(betw_cent.get(min(betw_cent))) + "\n\n")

    #write centralities to files
    with open('degree_centralities.txt', 'w') as f1:
        print("Writing degree centralities to a file...")
        f1.write(str(degr_cent))

    with open('eigvec_centralities.txt', 'w') as f2:
        print("Writing eigenvector centralities to a file...")
        f2.write(str(eigvec_cent))
    
    with open('betw_centralities.txt', 'w') as f3:
        print("Writing between centralities to a file...")
        f3.write(str(betw_cent))
    """
    #degree centrality histogram
    dc_degr_histogram = nx.degree_histogram(G)
    dc_degrees = range(len(dc_degr_histogram))

    """
    plt.figure(figsize=(12,8))
    plt.loglog(dc_degrees, dc_degr_histogram,'go-') 
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.savefig('degree_distribution.png')
    plt.show()
    

    
    #eigenvector centrality histogram
    eigenvec_degrees = range(len(eigvec_cent))
    print("This is eigenvec degr histogram", eigenvec_degrees)

    m = 3
    plt.figure(figsize=(12,8))
    plt.loglog(eigenvec_degrees, dc_degr_histogram,'go-') 
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.savefig('eigvec_distribution.png')
    plt.show()
    """
    degree_sequence = sorted((d for n,d in G.degree()), reverse=True)
    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    axgrid = fig.add_gridspec(5, 4)
    ax = fig.add_subplot()
    ax.bar(*np.unique(degree_sequence, return_counts=True))
    ax.set_title("Degree histogram")
    ax.set_xlabel("Degree")
    ax.set_ylabel("# of Nodes")
    plt.savefig('degree_distribution.png')
    plt.show()
    
    # IMPLEMENT THIS
    """
    eigvec_sequence = sorted((d for n,d in eigvec_cent.values()), reverse=True)
    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    axgrid = fig.add_gridspec(5, 4)
    ax = fig.add_subplot()
    ax.bar(*np.unique(eigvec_sequence, return_counts=True))
    ax.set_title("Eigenvec histogram")
    ax.set_xlabel("Degree")
    ax.set_ylabel("# of Nodes")
    plt.savefig('eigvec_distribution.png')
    plt.show()
    """

