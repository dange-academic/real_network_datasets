# -*- encoding: utf-8 -*-
'''
@File  :   read_data_to_network.py
@Date  :   2023/05/24 21:40:38
@Author:   chend
@Email :   chend_zqfpu@163.com
'''
import networkx as nx

# All the following networks are regarded as undirected networks


G = nx.read_edgelist('p2p-Gnutella04.txt', comments='#', create_using=nx.Graph()) 
# G = nx.read_edgelist('Internet (AS level) (1).txt', create_using=nx.Graph())
# G = nx.read_edgelist('Internet (AS level) (2).txt', comments='%', create_using=nx.Graph())
# G = nx.read_gml('as-22july06.gml')
# G = nx.read_edgelist('Google+ (NIPS).txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('Email-Enron.txt', comments='#', create_using=nx.Graph())
# G = nx.read_edgelist('web-baidu-baike-related.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('brightkite_edges.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('facebook-wosn-links.txt', comments='%', create_using=nx.Graph(), data=False)
# G = nx.read_edgelist('ca-AstroPh.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('youtube.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('Coauthor (2).txt', comments='#', create_using=nx.Graph())
# G = nx.read_edgelist('Actor.txt', create_using=nx.Graph())
# G = nx.read_edgelist('CA-CondMat.txt', comments='#', create_using=nx.Graph())
# G = nx.read_edgelist('ego-twitter.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('WWW (2).txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('Internet (router level).txt', create_using=nx.Graph())
# G = nx.read_edgelist('web-Stanford.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('WWW (4).txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('Protein folding.txt', comments='#', create_using=nx.Graph(), data=False)
# G = nx.read_edgelist('amazon.txt', comments='%', create_using=nx.Graph())



print(G)
avk = 2*nx.number_of_edges(G)/nx.number_of_nodes(G)
print("average degree: ", avk)