
import sample_path as sp
import networkx as nx
import os


class NetworkGraph():
    """
    Rappresenta un grafo dinamico con la seguente struttura:

        :sample_path: le traiettorie/a da cui costruire il grafo
        :graph: la struttura dinamica che definisce il grafo

    """

    def __init__(self, graph_struct):
        self.graph_struct = graph_struct
        self.graph = nx.DiGraph()


    def init_graph(self):
        #self.sample_path.build_trajectories()
        #self.sample_path.build_structure()
        self.add_nodes(self.graph_struct.list_of_nodes())
        self.add_edges(self.graph_struct.list_of_edges())

    def add_nodes(self, list_of_nodes):
        for indx, id in enumerate(list_of_nodes):
            #print(indx, id)
            self.graph.add_node(id)
            nx.set_node_attributes(self.graph, {id:indx}, 'indx')
        #for node in list(self.graph.nodes):
            #print(node)

    def add_edges(self, list_of_edges):
        self.graph.add_edges_from(list_of_edges)

    def get_ordered_by_indx_set_of_parents(self, node):
        ordered_set = {}
        parents = self.get_parents_by_id(node)
        for n in parents:
            indx = self.graph_struct.get_node_indx(n)
            ordered_set[n] = indx
        {k: v for k, v in sorted(ordered_set.items(), key=lambda item: item[1])}
        return list(ordered_set.keys())

    def get_ord_set_of_par_of_all_nodes(self):
        result = []
        for node in self.get_nodes():
            result.append(self.get_ordered_by_indx_set_of_parents(node))
        return result

    def get_nodes(self):
        return list(self.graph.nodes)

    def get_parents_by_id(self, node_id):
       return list(self.graph.predecessors(node_id))

    def get_states_number(self):
        return self.graph_struct.get_states_number()

    def get_node_by_index(self, node_id):
        return self.graph_struct.get_node_indx(node_id)


    



######Veloci Tests#######
"""os.getcwd()
os.chdir('..')
path = os.getcwd() + '/data'
s1 = sp.SamplePath(path)
s1.build_trajectories()
s1.build_structure()

g1 = NetworkGraph(s1.structure)
g1.init_graph()
print(g1.graph.number_of_nodes())
print(g1.graph.number_of_edges())

print(nx.get_node_attributes(g1.graph, 'indx')['X'])
for node in g1.get_parents_by_id('Z'):
    print(g1.get_node_by_index(node))
    print(node)
print(g1.get_ordered_by_indx_set_of_parents('Z'))
print(g1.get_ord_set_of_par_of_all_nodes())"""


