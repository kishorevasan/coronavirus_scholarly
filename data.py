import pandas as pd
from itertools import combinations
import networkx as nx

import community

data = pd.read_csv("metadata.csv")
data = data[['authors']]
tmp = data.shape[0]
data = data.dropna()

print "Total Number of Papers", tmp
print "Number of papers without authors:",tmp - data.shape[0]
print "Total number of papers with authors:", data.shape[0]

# Function to create the co-funding graph
# taken in the list of funders for each paper
# and returns a join list of co-funders
def get_coauthorship(x):
    global g
    authors = x.split(';')
    if len(authors)<2:
        return 1
    else:
        tmpcombs = list(combinations(authors, 2))
        for tmpcomb in tmpcombs:
            if not g.has_edge(tmpcomb[0], tmpcomb[1]):
                g.add_edge(tmpcomb[0],tmpcomb[1], weight = 0)
            #g[tmpcomb[0]][tmpcomb[1]]['weight']+=float(1)/float(len(words)-1)
            g[tmpcomb[0]][tmpcomb[1]]['weight']+=1
        return 2

# Create the co-funding network
g = nx.Graph(mode = "undirected", weighted = True)
res = data.authors.apply(get_coauthorship)
print res.to_frame().authors.value_counts()

print nx.info(g)

newg = max(nx.connected_component_subgraphs(g),key = len)

print nx.info(newg)

#part = community.community_louvain.best_partition(g)
#val = part.values()
#print "Modularity:", community.community_louvain.modularity(part,newg)
#print "Number of communities:", len(set(val))
#edges = list(g.edges())

#for i in range(len(edges)):
#  edges[i][2] = edges[i][2]['weight']

#print edges[:4]
