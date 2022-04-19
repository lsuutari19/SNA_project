# THIS IS OUR TO-DO LIST :)
Project 8. Graph and Semantic Analysis of Movie database 1
Explore the IMDB 5000 Movie database available at https://data.world/data-society/imdb5000-movie-dataset . The excel file can also be accessed at shared Google drive
https://1drv.ms/x/s!AtcJs3OTsMZuiRctyVt3IVt4lSup
The database contains several attributes for each movie, including main actor, second actor, third actor,
director, movie genre, various user ranking attributes, budget, keywords. We shall consider a network where
the nodes correspond to the actor names and the link is established whenever the two actors are played
together in at least one movie

Instructions:
1. Suggest appropriate preprocessing to make the dataset clean.
2. Use Networkx appropriate functions in order to study the properties of this network by
summarizing in a table its key characteristics, which contain: i) Number of nodes, ii) Number of
edges, iii) Overall clustering coefficient, iv) Diameter, v) Number of components and size of its
largest component, vi) Average path length, vii) Maximum degree, average degree, and minimum
degree centrality; vii) maximum / average and minimum eigen vector centrality, ix) maximum /
average / minimum betweenness centrality.
3. Save in a file the degree centrality of each node and draw the degree distribution. Then check
whether a power-law distribution can be fitted or not. Justify your answer
4. Save in a file the result of eigenvector centrality of each node. Suggest a subdivision (histogram
bins) of these values that take into account the variability of the centrality values. Draw the
corresponding degree distribution and check whether a power law can be fit.
5. Repeat question 4) when using betweenness centrality.
6. Provide the ten highly ranked actors according to each of the centrality measure: degree
centrality, eigenvector centrality, betweenness centrality. Comment on the overlapping and
discrepancy between the three centrality measures.
7. Use appropriate NetworkX functions to determine communities using clique, k-clique, and GirvanNewman algorithms. Summarize in a table the main characteristics of each community.
8. We would like to investigate the communities identified by those algorithms for the original
movie network. For this purpose, we would like to test some hypotheses. The first hypothesis is
that the community corresponds to movies belonging to same category, e.g., Action movies,
Romance, Science Fiction, etc. The second hypothesis is that community corresponds to movies
belonging to same series (episode). Use the information of your movie database that you have
selected (e.g., Internet Movie Database) to test the two hypotheses. Propose a more formal
evaluations.
9. Discuss whether some communities match other attributes of the database (keywords, genre,
country, budget..)
10. Provide a methodology and a script that computes actor ranking based on the ranking of movies the
actor has participated (a simple way to do so is to average the ranking of movies the actor is
involved with but other options are also possible).
11. Now we would like to compare how the ranking data matches with various centrality measures in
order to identify whether a given centrality measure better agrees with the ranking outcomes. For
this purpose, construct a histogram distribution showing the proportion of actors whose ranking
values fall within a given subdivision of the histogram (you should transform the ranking data into a
normalized scale, e.g., within [0,1] interval in order to ease comparison with other measures).
Similarly, construct for each centrality measure in 1) a histogram showing the proportion of the
actors whose centrality measure falls within the corresponding histogram bin. Again for ease of
comparison, the centrality measures should be transformed to normalized scale. Finally use a simple
distance between histograms in order to calculate the distance between the ranking histogram and
the underlined centrality measure. Identify the best matching centrality measure accordingly.
10. Use potential literature from entertainment and movie making in order to comprehend the results of
your finding.

### Todo

  - [ ] Bonus: Remove incomplete lines w/ Python

### In Progress

- [ ] Mikko on päästetty aitauksesta työskentelmään
- [ ] Debugging task 2 (formNetwork.py)
  - [ ] checking that the values are correct (can be done by reducing sheet.nrows = 5 and manually calculating
      - [ ] for example the average centralities are currently done wrong
  - [ ] save in a file all the centralities and draw the degree distributions (instructions 3-5)
### Done ✓

- [✓] 13/4/22 meeting   
- [✓] Remove incomplete lines
- [✓] Removed the odd characters at the end of movie titles
- [✓] IMDB scores fixed
- [✓] Get familiar :) w/ dataset
- [✓] Clean the excel
