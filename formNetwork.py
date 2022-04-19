import networkx as nx
import matplotlib.pyplot as plt
import xlrd

file = "./databases/NEC.xls"

G = nx.Graph()
names = []

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(1)

#columns are 6 and 10 for actor2 and actor1 respectively
for row in range(sheet.nrows):
    data = sheet.row_slice(row)
    person1 = data[6].value
    person2 = data[10].value
    #appends a tupple person1,person2 to list
    names.append( (person1, person2) )

#print(names)

G.add_edges_from(names)
nx.draw(G, with_labels=True)
plt.show()