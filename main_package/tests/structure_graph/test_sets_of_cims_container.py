import sys
sys.path.append("../../classes/")
import unittest
import structure_graph.set_of_cims as sc
import structure_graph.sets_of_cims_container as scc


class TestSetsOfCimsContainer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.variables = ['X', 'Y', 'Z']
        cls.states_per_node = [3, 3, 3]
        cls.parents_states_list = [[], [3], [3, 3]]

    def test_init(self):
        #TODO: Fix this initialization
        c1 = scc.SetsOfCimsContainer(self.variables, self.states_per_node, self.parents_states_list)
        self.assertEqual(len(c1.sets_of_cims), len(self.variables))
        for set_of_cims in c1.sets_of_cims:
            self.assertIsInstance(set_of_cims, sc.SetOfCims)



if __name__ == '__main__':
    unittest.main()