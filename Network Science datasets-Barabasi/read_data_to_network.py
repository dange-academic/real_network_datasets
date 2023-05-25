# -*- encoding: utf-8 -*-
'''
@File  :   read_data_to_network.py
@Date  :   2023/05/24 21:40:38
@Author:   chend
@Email :   chend_zqfpu@163.com
'''
import networkx as nx

# # undirected networks
# G = nx.read_edgelist('internet.txt', create_using=nx.Graph()) 

# print(G)
# avk = 2*nx.number_of_edges(G)/nx.number_of_nodes(G)
# print("average degree: ", avk)


# directed networks
G = nx.read_edgelist('www.txt', create_using=nx.DiGraph()) 
print(G)
avk = nx.number_of_edges(G)/nx.number_of_nodes(G)
print("average degree: ", avk)