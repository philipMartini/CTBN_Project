import unittest
import networkx as nx

import sample_path as sp
import network_graph as ng


class TestNetworkGraph(unittest.TestCase):

    def setUp(self):
        self.s1 = sp.SamplePath('../data', 'samples', 'dyn.str', 'variables', 'Time', 'Name')
        self.s1.build_trajectories()
        self.s1.build_structure()

    def test_init(self):
        g1 = ng.NetworkGraph(self.s1.structure)
        self.assertEqual(self.s1.structure, g1.graph_struct)
        self.assertIsInstance(g1.graph, nx.DiGraph)
        #TODO MANCANO TUTTI I TEST DI INIZIALIZZAZIONE DEI DATI PRIVATI della classe aggiungere le property necessarie

    def test_add_nodes(self):
        g1 = ng.NetworkGraph(self.s1.structure)
        g1.add_nodes(self.s1.structure.list_of_nodes_labels())
        for n1, n2 in zip(g1.get_nodes(), self.s1.structure.list_of_nodes_labels()):
            self.assertEqual(n1, n2)

    def test_add_edges(self):
        g1 = ng.NetworkGraph(self.s1.structure)
        g1.add_edges(self.s1.structure.list_of_edges())
        for e in self.s1.structure.list_of_edges():
            self.assertIn(tuple(e), g1.get_edges())

    def test_get_ordered_by_indx_set_of_parents(self):
        g1 = ng.NetworkGraph(self.s1.structure)
        g1.add_nodes(self.s1.structure.list_of_nodes_labels())
        g1.add_edges(self.s1.structure.list_of_edges())
        sorted_par_list_aggregated_info = g1.get_ordered_by_indx_set_of_parents(g1.get_nodes()[2])
        self.test_aggregated_par_list_data(g1,g1.get_nodes()[2], sorted_par_list_aggregated_info)

    def test_aggregated_par_list_data(self, graph, node_id, sorted_par_list_aggregated_info):
        for indx, element in enumerate(sorted_par_list_aggregated_info):
            if indx == 0:
                self.assertEqual(graph.get_parents_by_id(node_id), element)
                for j in range(0, len(sorted_par_list_aggregated_info[0]) - 1):
                    self.assertLess(self.s1.structure.get_node_indx(sorted_par_list_aggregated_info[0][j]),
                                    self.s1.structure.get_node_indx(sorted_par_list_aggregated_info[0][j + 1]))
            elif indx == 1:
                for node, node_indx in zip(sorted_par_list_aggregated_info[0], sorted_par_list_aggregated_info[1]):
                    self.assertEqual(graph.get_node_indx(node), node_indx)
            else:
                for node, node_val in zip(sorted_par_list_aggregated_info[0], sorted_par_list_aggregated_info[2]):
                    self.assertEqual(graph.graph_struct.get_states_number(node), node_val)

    def test_get_ord_set_of_par_of_all_nodes(self):
        g1 = ng.NetworkGraph(self.s1.structure)
        g1.add_nodes(self.s1.structure.list_of_nodes_labels())
        g1.add_edges(self.s1.structure.list_of_edges())
        sorted_list_of_par_lists = g1.get_ord_set_of_par_of_all_nodes()
        for node, par_list in zip(g1.get_nodes_sorted_by_indx(), sorted_list_of_par_lists):
            self.test_aggregated_par_list_data(g1, node, par_list)

    def test_get_ordered_by_indx_parents_values_for_all_nodes(self):
        g1 = ng.NetworkGraph(self.s1.structure)
        g1.add_nodes(self.s1.structure.list_of_nodes_labels())
        g1.add_edges(self.s1.structure.list_of_edges())
        g1.aggregated_info_about_nodes_parents = g1.get_ord_set_of_par_of_all_nodes()
        print(g1.get_ordered_by_indx_parents_values_for_all_nodes())


if __name__ == '__main__':
    unittest.main()