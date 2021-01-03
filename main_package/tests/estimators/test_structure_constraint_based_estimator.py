import sys
sys.path.append("../../classes/")
import glob
import math
import os
import unittest

import networkx as nx
import numpy as np
import psutil
from line_profiler import LineProfiler

import utility.cache as ch
import structure_graph.sample_path as sp
import estimators.structure_constraint_based_estimator as se
import utility.json_importer as ji

from multiprocessing import set_start_method

import copy


class TestStructureConstraintBasedEstimator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.read_files = glob.glob(os.path.join('../../data', "*.json"))
        cls.importer = ji.JsonImporter("../../data/networks_and_trajectories_ternary_data_15.json", 'samples', 'dyn.str', 'variables', 'Time', 'Name',1)
        cls.s1 = sp.SamplePath(cls.importer)
        cls.s1.build_trajectories()
        cls.s1.build_structure()

    def test_structure(self):
        true_edges = copy.deepcopy(self.s1.structure.edges)
        true_edges = set(map(tuple, true_edges))

        set_start_method("spawn")
        se1 = se.StructureConstraintBasedEstimator(self.s1,0.1,0.1)
        edges = se1.estimate_structure(disable_multiprocessing=False)
        

        self.assertEqual(edges, true_edges)

if __name__ == '__main__':
    unittest.main()