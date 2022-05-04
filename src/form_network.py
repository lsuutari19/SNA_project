#!/usr/bin/env python

"""
This file is for Social Network Analysis
project work, where movie database is analysed.
"""

import statistics
from itertools import chain
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import xlrd
import networkx.algorithms.community as nxac
from constants import (
    FILE,
    RESULTS,
    RESULT_PREFIX,
    BETWEENNES_FILE,
    DEGREE_FILE,
    EIGEN_FILE,
    RESULTS_FILE,
    DEG_DISTR,
    EIG_DISTR,
    BETW_DISTR,
    CLIQUE_FILE,
    K_CLIQUE_FILE,
    GIRVAN_FILE,
    BETWEENNES_RANKED,
    DEGREE_RANKED,
    EIGEN_RANKED,
)
from utils import generate_graph, init_result, write_result, sort_centralities



class NetworkHandler:
    """
    Contains methods for generating information
    from Movie database
    """

    def __init__(self) -> None:
        """
        Inits the class with Graph and datasheet
        """
        self.graph = nx.Graph()
        self.book = xlrd.open_workbook(FILE)
        self.sheet = self.book.sheet_by_index(1)
        generate_graph(self.graph, self.sheet)
        self.degr_cent = nx.degree_centrality(self.graph)
        self.eigvec_cent = nx.eigenvector_centrality(self.graph)
        self.betw_cent = nx.betweenness_centrality(self.graph)

    def calculate_network_properties(self):
        """
        Calculates the basic properties of the network,
        mentioned in step 2 of the README.md instructions
        """
        # Init result files before calculating new values
        init_result(BETWEENNES_FILE, "")
        init_result(DEGREE_FILE, "")
        init_result(EIGEN_FILE, "")
        init_result(RESULTS_FILE, "")
        init_result(BETWEENNES_RANKED, "")
        init_result(DEGREE_RANKED, "")
        init_result(EIGEN_RANKED, "")
        # 1. Number of Nodes
        num_of_nodes = "number of nodes: " + str(self.graph.number_of_nodes()) + "\n"
        RESULTS.append(num_of_nodes)
        # 2. Number of Edges
        num_of_edges = "number of edges: " + str(self.graph.number_of_edges()) + "\n"
        RESULTS.append(num_of_edges)
        # 3. Clustering coefficient
        clust_coeff = (
            "clustering coefficient: " + str(nx.average_clustering(self.graph)) + "\n"
        )
        RESULTS.append(clust_coeff)
        # 4. Diameter of the Graph
        diameter = max(
            [max(j.values()) for (i, j) in nx.shortest_path_length(self.graph)]
        )
        graph_diameter = "diameter: " + str(diameter) + "\n"
        RESULTS.append(graph_diameter)
        # 5. Number of components
        num_of_components = (
            "number of components: "
            + str(nx.number_connected_components(self.graph))
            + "\n"
        )
        RESULTS.append(num_of_components)
        # 6. Largest component
        largest_component = (
            "largest component: "
            + str(max(nx.connected_components(self.graph), key=len))
            + "\n"
        )
        RESULTS.append(largest_component)
        # 7. Average Path length
        path_lengths = (j.values() for (i, j) in nx.shortest_path_length(self.graph))
        avg_path_len = statistics.mean(chain.from_iterable(path_lengths))
        average_path_length = "avg path length: " + str(avg_path_len) + "\n"
        RESULTS.append(average_path_length)
        # 8. Degree centrality
        RESULTS.append(
            "minimum degree centrality: "
            + str(max(self.degr_cent))
            + " "
            + str(self.degr_cent.get(max(self.degr_cent)))
            + "\n"
        )
        RESULTS.append(
            "maximum degree centrality: "
            + str(min(self.degr_cent))
            + " "
            + str(self.degr_cent.get(min(self.degr_cent)))
            + "\n"
        )
        avg_degr_cent = sum(self.degr_cent.values()) / len(self.degr_cent)
        RESULTS.append("average degree centrality: " + str(avg_degr_cent) + "\n\n")
        # 9. Eigenvector centrality
        RESULTS.append(
            "minimum eigenvector centrality: "
            + str(min(self.eigvec_cent))
            + " "
            + str(self.eigvec_cent.get(min(self.eigvec_cent)))
            + "\n"
        )
        RESULTS.append(
            "maximum eigenvector centrality: "
            + str(max(self.eigvec_cent))
            + " "
            + str(self.eigvec_cent.get(max(self.eigvec_cent)))
            + "\n"
        )
        avg_eigvec_cent = sum(self.eigvec_cent.values()) / len(self.eigvec_cent)
        RESULTS.append(
            "average eigenvector centrality: " + str(avg_eigvec_cent) + "\n\n"
        )
        # 10. Betweennes centrality
        RESULTS.append(
            "minimum betweenness centrality: "
            + str(min(self.betw_cent))
            + " "
            + str(self.betw_cent.get(min(self.betw_cent)))
            + "\n"
        )
        RESULTS.append(
            "maximum betweenness centrality: "
            + str(max(self.betw_cent))
            + " "
            + str(self.betw_cent.get(max(self.betw_cent)))
            + "\n"
        )
        avg_betw_cent = sum(self.betw_cent.values()) / len(self.betw_cent)
        RESULTS.append("average betweenness centrality: " + str(avg_betw_cent) + "\n\n")

        # Sort the centrality_data and write them to files
        betw_sorted = sort_centralities(self.betw_cent)
        degree_sorted = sort_centralities(self.degr_cent)
        eigveg_sorted = sort_centralities(self.eigvec_cent)

        write_result(BETWEENNES_RANKED, str(betw_sorted))
        write_result(DEGREE_RANKED, str(degree_sorted))
        write_result(EIGEN_RANKED, str(eigveg_sorted))

        # Write the RESULTS to a FILE
        for result in RESULTS:
            write_result(RESULTS_FILE, result)

        write_result(BETWEENNES_FILE, str(self.betw_cent))
        write_result(DEGREE_FILE, str(self.degr_cent))
        write_result(EIGEN_FILE, str(self.eigvec_cent))

    def generate_degree_distribution_graph(self):
        """
        Generates degree distribution graph
        """
        degree_sequence = sorted((d for n, d in self.graph.degree()), reverse=True)
        fig = plt.figure("Degree of a random graph", figsize=(8, 8))
        x_axis = fig.add_subplot()
        x_axis.plot(*np.unique(degree_sequence, return_counts=True))
        x_axis.set_title("Degree histogram")
        x_axis.set_xlabel("Degree")
        x_axis.set_ylabel("# of Nodes")
        plt.savefig(RESULT_PREFIX + DEG_DISTR)
        plt.show()

    def generate_eigenvector_distribution_graph(self):
        """
        Generates Eigenvector distribution graph
        """
        eigvec_sequence = sorted((d for d in self.eigvec_cent.values()), reverse=True)
        fig = plt.figure("Degree of a random graph", figsize=(8, 8))
        x_axis = fig.add_subplot()
        x_axis.set_title("Eigenvec histogram")
        x_axis.set_xlabel("Degree")
        x_axis.set_ylabel("# of Nodes")
        plt.hist(eigvec_sequence, bins=100)
        plt.savefig(RESULT_PREFIX + EIG_DISTR)
        plt.show()

    def generate_betweennes_distribution_graph(self):
        """
        Generates Betweennes distribution graph
        """
        betw_sequence = sorted((d for d in self.betw_cent.values()), reverse=True)
        fig = plt.figure("Degree of random graph", figsize=(8, 8))
        x_axis = fig.add_subplot()
        x_axis.set_title("Betweennes histogram")
        x_axis.set_xlabel("Degree")
        x_axis.set_ylabel("# of Nodes")
        plt.hist(betw_sequence, bins=100)
        plt.savefig(RESULT_PREFIX + BETW_DISTR)
        plt.show()

    def generate_communities(self):
        # this is all the communities, calculation cliques can be done in two ways
        # girvan newman is not possible bc of time complexity
        #write_result(CLIQUE_FILE, str(list(nx.enumerate_all_cliques(self.graph))))
        write_result(CLIQUE_FILE, str(list(nx.find_cliques(self.graph))))
        write_result(K_CLIQUE_FILE, str(list(nxac.k_clique_communities(self.graph, 2))))
        #write_result(GIRVAN_FILE, str(list(nxac.girvan_newman(self.graph))))

def main():
    """
    Main program function
    Contains all the class methods needed to generate data from the social network
    """
    network = NetworkHandler()
<<<<<<< HEAD
    #network.generate_betweennes_distribution_graph()
    #network.generate_eigenvector_distribution_graph()
    #network.generate_degree_distribution_graph()
=======
    #    network.generate_betweennes_distribution_graph()
    #    network.generate_eigenvector_distribution_graph()
    #    network.generate_degree_distribution_graph()

    network.calculate_network_properties()
>>>>>>> 886ebbef0df5dcbc9f2457252eb215ec446eb5ef

    #network.calculate_network_properties()
    network.generate_communities()

if __name__ == "__main__":
    main()
