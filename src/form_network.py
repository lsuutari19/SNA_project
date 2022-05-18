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
from sklearn import preprocessing

from constants import (
    DEGREE_RANKED_REAL_CENT,
    FILE,
    FILE2,
    GENRE_RESULTS,
    GENRES_FILE,
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
    RANKS_FILE,
    IMDB_DISTR,
    MANY_DISTR,
)
from utils import (
    generate_graph,
    init_result,
    write_result,
    sort_centralities,
    generate_genre_graph,
    generate_rank_dict,
    normalize,
    generate_genre_relations,
)


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
        self.genre_graph = nx.Graph()
        self.book = xlrd.open_workbook(FILE)
        self.sheet = self.book.sheet_by_index(1)
        generate_graph(self.graph, self.sheet)
        generate_genre_graph(self.genre_graph, self.sheet)
        generate_genre_relations(self.genre_graph, self.sheet)
        self.degr_cent = nx.degree_centrality(self.graph)
        self.real_degr_cent = nx.degree(self.graph)
        self.eigvec_cent = nx.eigenvector_centrality(self.graph)
        self.betw_cent = nx.betweenness_centrality(self.graph)

    def calculate_genre_properties(self):
        """
        Calculates properties for Genre graph
        """
        # Init results for genre graph
        init_result(GENRES_FILE, "")
        num_of_nodes = (
            "number of nodes: " + str(self.genre_graph.number_of_nodes()) + "\n"
        )
        GENRE_RESULTS.append(num_of_nodes)
        write_result(GENRES_FILE, str(num_of_nodes))

        # this is all the communities, calculation cliques can be done in two ways
        # girvan newman is not possible bc of time complexity
        write_result(GENRES_FILE, str(list(nx.enumerate_all_cliques(self.genre_graph))))
        cliques = sorted(list(nx.find_cliques(self.genre_graph)), reverse=True)
        k_cliques = sorted(
            [list(x) for x in nxac.k_clique_communities(self.genre_graph, 5)],
            reverse=True,
        )
        print(max(cliques, key=len))
        write_result(GENRES_FILE, str(cliques))

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
        init_result(DEGREE_RANKED_REAL_CENT, "")
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
        largest_c = max(nx.connected_components(self.graph), key=len)
        print("Largest component: " + str(len(largest_c)))
        size_of_largest_component = (
            "Size of the largest component: " + str(len(list(largest_c))) + "\n"
        )
        RESULTS.append(size_of_largest_component)
        RESULTS.append(largest_component)
        # 7. Average Path length
        path_lengths = (j.values() for (i, j) in nx.shortest_path_length(self.graph))
        avg_path_len = statistics.mean(chain.from_iterable(path_lengths))
        average_path_length = "avg path length: " + str(avg_path_len) + "\n"
        RESULTS.append(average_path_length)
        # 8. Degree centrality
        RESULTS.append(
            "minimum degree centrality: " + str(min(self.degr_cent.values())) + "\n"
        )
        RESULTS.append(
            "maximum degree centrality: " + str(max(self.degr_cent.values())) + "\n"
        )
        avg_degr_cent = sum(self.degr_cent.values()) / len(self.degr_cent)
        RESULTS.append("average degree centrality: " + str(avg_degr_cent) + "\n\n")
        # 9. Eigenvector centrality
        RESULTS.append(
            "minimum eigenvector centrality: "
            + str(min(self.eigvec_cent.values()))
            + "\n"
        )
        RESULTS.append(
            "maximum eigenvector centrality: "
            + str(max(self.eigvec_cent.values()))
            + "\n"
        )
        avg_eigvec_cent = sum(self.eigvec_cent.values()) / len(self.eigvec_cent)
        RESULTS.append(
            "average eigenvector centrality: " + str(avg_eigvec_cent) + "\n\n"
        )
        # 10. Betweennes centrality
        RESULTS.append(
            "minimum betweenness centrality: "
            + str(min(self.betw_cent.values()))
            + "\n"
        )
        RESULTS.append(
            "maximum betweenness centrality: "
            + str(max(self.betw_cent.values()))
            + "\n"
        )
        avg_betw_cent = sum(self.betw_cent.values()) / len(self.betw_cent.values())
        RESULTS.append("average betweenness centrality: " + str(avg_betw_cent) + "\n\n")

        # Sort the centrality_data and write them to files
        betw_sorted = sort_centralities(self.betw_cent)
        degree_sorted = sort_centralities(self.degr_cent)
        eigveg_sorted = sort_centralities(self.eigvec_cent)

        sorted_real_cent = [
            (actor, degree)
            for (actor, degree) in sorted(
                self.real_degr_cent,
                key=lambda connect: connect[1],
                reverse=True,
            )
        ]
        # Write results of Degree centrality with nx.degree()
        write_result(DEGREE_RANKED_REAL_CENT, str(sorted_real_cent))

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
        """
        Generate communities from the Graph
        """
        init_result(CLIQUE_FILE, "")
        init_result(K_CLIQUE_FILE, "")
        # this is all the communities, calculation cliques can be done in two ways
        # girvan newman is not possible bc of time complexity
        write_result(CLIQUE_FILE, str(list(nx.enumerate_all_cliques(self.graph))))
        cliques = sorted(list(nx.find_cliques(self.graph)), reverse=True)
        x_axis = self.genre_graph
        y_axis = sorted(list(nx.find_cliques(self.genre_graph)), reverse=True)
 
        #print("\n\nthese are cliques: ", y_axis, "\n\n")
        k_cliques_genres = sorted(
            [list(x) for x in nxac.k_clique_communities(self.genre_graph, 5)],
            reverse=True,
        )
        print("these are k-cliques: ", k_cliques_genres, "\n\n")
        k_cliques = sorted(
            [list(x) for x in nxac.k_clique_communities(self.graph, 5)],
            reverse=True,
        )
        print(max(cliques, key=len))
        print(max(k_cliques, key=len))
        write_result(CLIQUE_FILE, str(cliques))
        write_result(K_CLIQUE_FILE, str(k_cliques))
        # Commented out because of time complexity
        # write_result(GIRVAN_FILE, str(list(nxac.girvan_newman(self.graph))))

    def actor_rankings(self):
        file = open("results/" + RANKS_FILE, "r+")
        file.truncate(0)
        file.close()
        self.book2 = xlrd.open_workbook(FILE2)
        self.sheet2 = self.book2.sheet_by_index(1)
        rank_dict = generate_rank_dict(self.sheet2)
        write_result(
            RANKS_FILE,
            {k: v for k, v in sorted(rank_dict.items(), key=lambda item: item[1])},
        )
        print(len(rank_dict.keys()))
        fig, ax = plt.subplots(figsize=(8, 8))
        data = rank_dict.values()
        data_list = list(data)
        arr = np.array(data_list)
        normalized_arr = (arr - np.min(arr) / np.max(arr) - np.min(arr)) / 10

        ax.hist(normalized_arr, bins=100, label="actor rank")
        ax.set_title("Normalized IMDb scores compared with normalized centralities")
        ax.set_xlabel("Normalized values")
        ax.set_ylabel("# of Actors")
        plt.savefig(RESULT_PREFIX + IMDB_DISTR)

        betw_sequence = sorted((d for d in self.betw_cent.values()), reverse=True)
        norm_betw_seq = normalize(betw_sequence)
        plt.hist(norm_betw_seq, bins=100, label="betweenness")

        eigvec_sequence = sorted((d for d in self.eigvec_cent.values()), reverse=True)
        norm_eigvec_seq = normalize(eigvec_sequence)
        plt.hist(norm_eigvec_seq, bins=100, label="eigen vector")

        degree_sequence = sorted((d for n, d in self.graph.degree()), reverse=True)
        norm_degree_seq = normalize(degree_sequence)
        plt.hist(norm_degree_seq, bins=100, label="degree")
        plt.legend()
        plt.savefig(RESULT_PREFIX + MANY_DISTR)
        plt.show()


def main():
    """
    Main program function
    Contains all the class methods needed to generate data from the social network
    """
    network = NetworkHandler()
    network.generate_betweennes_distribution_graph()
    network.generate_eigenvector_distribution_graph()
    network.generate_degree_distribution_graph()

    network.calculate_network_properties()
    network.calculate_genre_properties()

    network.generate_communities()
    network.actor_rankings()

    print("\n\nCheck results folder for the results of the program.")

if __name__ == "__main__":
    main()
