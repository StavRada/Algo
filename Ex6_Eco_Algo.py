from typing import List

import networkx as nx



def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    G = nx.Graph()
    Players = len(allocation)
    Items = len(allocation[0])

    # fill the graph with players and items
    for i in range(Players):
        G.add_node("player:" + str(i))
    for j in range(Items):
        G.add_node("item:" + str(j))

        if 0 < allocation[i][j] <= 1:
            G.add_edge(i, j)

    # checking if cycle exists
    try:
        print(list(nx.find_cycle(G, orientation="ignore")))
    except:
        print("no cycles")


if __name__ == '__main__':

    find_cycle_in_consumption_graph([[0, 0.05, 0.4, 0], [1, 0.95, 0.6, 1]])

    find_cycle_in_consumption_graph([[0, 1, 0.4, 0], [1, 4, 0.6, 1]])

    find_cycle_in_consumption_graph([[1, 0.5, 0.25, 0],
                                     [0, 0, 0.75, 0.5],
                                     [0, 0, 0.25, 0.5],
                                     [0, 0.5, 0, 0]])

    find_cycle_in_consumption_graph([[1, 1, 0, 0.25, 0.15, 0.5],
                                     [0, 0, 0, 0.25, 0.15, 0.25],
                                     [0, 0, 1, 0.5, 0.7, 0.25]])

    find_cycle_in_consumption_graph([[1, 1, 0.25, 0],
                                    [0, 0, 0.75, 0.5],
                                    [0, 0, 0.25, 0.5]])

    find_cycle_in_consumption_graph([[1, 0.5, 0.25, 0],
                                     [0, 0, 0.75, 0.5],
                                     [0, 0, 0.25, 0.5],
                                     [0, 0.5, 0, 0]])