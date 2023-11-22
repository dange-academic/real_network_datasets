# -*- encoding: utf-8 -*-
'''
@File  :   read_data_to_network.py
@Date  :   2023/05/24 21:40:38
@Author:   chend
@Email :   chend_zqfpu@163.com
'''
import networkx as nx

# All the following networks are regarded as undirected networks


G = nx.read_edgelist('./PRE2020/p2p-Gnutella04.txt', comments='#', create_using=nx.Graph()) 
# G = nx.read_edgelist('./PRE2020/Internet (AS level) (1).txt', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/Internet (AS level) (2).txt', comments='%', create_using=nx.Graph())
# G = nx.read_gml('./PRE2020/as-22july06.gml')
# G = nx.read_edgelist('./PRE2020/Google+ (NIPS).txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/Email-Enron.txt', comments='#', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/web-baidu-baike-related.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/brightkite_edges.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/facebook-wosn-links.txt', comments='%', create_using=nx.Graph(), data=False)
# G = nx.read_edgelist('./PRE2020/ca-AstroPh.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/youtube.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/Coauthor (2).txt', comments='#', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/Actor.txt', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/CA-CondMat.txt', comments='#', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/ego-twitter.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/WWW (2).txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/Internet (router level).txt', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/web-Stanford.txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/WWW (4).txt', comments='%', create_using=nx.Graph())
# G = nx.read_edgelist('./PRE2020/Protein folding.txt', comments='#', create_using=nx.Graph(), data=False)
# G = nx.read_edgelist('./PRE2020/amazon.txt', comments='%', create_using=nx.Graph())



print(G)
avk = 2*nx.number_of_edges(G)/nx.number_of_nodes(G)
print("average degree: ", avk)