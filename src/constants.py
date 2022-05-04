"""
Constants for form_network.py
Filelocations and result list
for appending data
"""

# Database file
FILE = "../databases/NEC.xls"
# Results folder prefix for saving results
RESULT_PREFIX = "../results/"
# For saving the lines to write to results folder files
RESULTS = []

# Datafiles
BETWEENNES_FILE = "betw_centralities.txt"
DEGREE_FILE = "degree_centralities.txt"
EIGEN_FILE = "eigveg_centralities.txt"
RESULTS_FILE = "result.txt"

# High ranked files
BETWEENNES_RANKED = "betw_ranked_actors.txt"
DEGREE_RANKED = "degree_ranked_actors.txt"
EIGEN_RANKED = "eigveg_ranked_actors.txt"

# Data distribution graphs
DEG_DISTR = "degree_distribution.png"
EIG_DISTR = "eigvec_distribution.png"
BETW_DISTR = "betw_distribution.png"
