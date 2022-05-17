"""
Constants for form_network.py
Filelocations and result list
for appending data
"""

# Database file
FILE = "databases/NEC.xls"
FILE2 = "databases/RankingActors.xls"
# Results folder prefix for saving results
RESULT_PREFIX = "results/"
# For saving the lines to write to results folder files
RESULTS = []
GENRE_RESULTS = []

# Datafiles
BETWEENNES_FILE = "betw_centralities.txt"
DEGREE_FILE = "degree_centralities.txt"
EIGEN_FILE = "eigveg_centralities.txt"
RESULTS_FILE = "result.txt"
CLIQUE_FILE = "clique_communities.txt"
GIRVAN_FILE = "girvan_newman_communities.txt"
K_CLIQUE_FILE = "k_clique_communities.txt"
GENRES_FILE = "genre_results.txt"
RANKS_FILE = "actor_ranks.txt"

# High ranked files
BETWEENNES_RANKED = "betw_ranked_actors.txt"
DEGREE_RANKED = "degree_ranked_actors.txt"
DEGREE_RANKED_REAL_CENT = "real_degr_cent.txt"
EIGEN_RANKED = "eigveg_ranked_actors.txt"

# Data distribution graphs
DEG_DISTR = "degree_distribution.png"
EIG_DISTR = "eigvec_distribution.png"
BETW_DISTR = "betw_distribution.png"
IMDB_DISTR = "imdb_distribution.png"
MANY_DISTR = "many_distributions.png"