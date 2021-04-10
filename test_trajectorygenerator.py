import unittest
import random

from PyCTBN.PyCTBN.structure_graph.trajectory_generator import TrajectoryGenerator
from PyCTBN.PyCTBN.utility.json_importer import JsonImporter

class TestTrajectoryGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.j1 = JsonImporter("./PyCTBN/test_data/networks_and_trajectories_binary_data_01_3.json", "samples", "dyn.str", "variables", "Time", "Name")

    def test_init(self):
        tg = TrajectoryGenerator(self.j1)
        self.assertEqual(len(tg._vnames), len(self.j1.variables))
        self.assertIsInstance(tg._vnames, list)
        self.assertIsInstance(tg._parents, dict)
        self.assertIsInstance(tg._cims, dict)
        self.assertListEqual(list(tg._parents.keys()), tg._vnames)
        self.assertListEqual(list(tg._cims.keys()), tg._vnames)

    def test_generated_trajectory(self):
        tg = TrajectoryGenerator(self.j1)
        end_time = random.randint(5, 100)
        sigma = tg.CTBN_Sample(end_time)
        self.assertLessEqual(sigma.times[len(sigma.times) - 1], end_time)
        for index in range(len(sigma.times)):
            if index > 0:
                self.assertLess(sigma.times[index - 1], sigma.times[index])
                diff = abs(sum(sigma.trajectory[index - 1]) - sum(sigma.trajectory[index]))
                self.assertEqual(diff, 1)

    def test_generated_trajectory_max_tr(self):
        tg = TrajectoryGenerator(self.j1)
        n_tr = random.randint(5, 100)
        sigma = tg.CTBN_Sample(max_tr = n_tr)
        self.assertEqual(len(sigma.times), n_tr + 1)

unittest.main()