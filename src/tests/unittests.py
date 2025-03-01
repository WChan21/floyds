"""
Unit test for the recursive Floyd-Warshall algorithm.
"""

import unittest
import sys
import os
from io import StringIO


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


try:
    from src.recursion.recursive_floyd import recursive_floyd_warshall, GRAPH, NO_PATH
except ModuleNotFoundError:
    from recursion.recursive_floyd import recursive_floyd_warshall, GRAPH, NO_PATH

class TestRecursiveFloydWarshall(unittest.TestCase):
    """
    Unit test for the recursive Floyd-Warshall implementation.
    """

    def setUp(self):
        """
        Reset the global GRAPH before each test.
        """
        global GRAPH
        GRAPH[:] = [  
            [0,   7,  NO_PATH, 8],
            [NO_PATH, 0, 5,  NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

       
        self.expected_result = [
            [0,  7,  12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

    def test_recursive_floyd(self):
        """
        Test the recursive Floyd-Warshall implementation.
        """
        recursive_floyd_warshall(0, 0, 0)  
        self.assertEqual(GRAPH, self.expected_result)  

if __name__ == "__main__":
    unittest.main()
