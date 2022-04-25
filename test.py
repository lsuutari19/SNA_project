import networkx as nx
from networkx.algorithms import bipartite
import pandas as pd
import matplotlib.pyplot as plt

graded_graph = nx.Graph()
graded_graph.add_nodes_from(["actor_1", "actor_5", "actor_10", "actor_11"], bipartite=0)
graded_graph.add_nodes_from(
    ["mov_1", "mov_2", "mov_4", "mov_6", "mov_5", "mov_8"], bipartite=1
)
graded_graph.add_edges_from(
    [
        ("actor_1", "mov_1"),
        ("actor_1", "mov_2"),
        ("actor_1", "mov_4"),
        ("actor_11", "mov_6"),
        ("actor_5", "mov_5"),
        ("actor_10", "mov_8"),
    ]
)


nx.draw(graded_graph, with_labels=True)
plt.show()

gd = graded_graph.to_directed()
dfDegree = pd.DataFrame(
    [
        {"name": v[0][0], "degree": v[0][1], "type": v[0][0].split("_")[0]}
        for v in list(zip(gd.degree))
    ]
)
dfDegreeActor = dfDegree.query('type=="actor"')
dfDegreeMov = dfDegree.query('type=="mov"')
print(dfDegreeActor)
print(dfDegreeMov)
