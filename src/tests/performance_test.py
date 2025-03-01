"""
This module contains a simple performance test which
compares the recursive version of Floyd's algorithm with the
imperative version.
"""

import sys
import os
from time import process_time


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


try:
    from src.recursion.recursive_floyd import recursive_floyd_warshall
    from src.iterative.iterative_floyd import iterative_floyd
except ModuleNotFoundError:
    from recursion.recursive_floyd import recursive_floyd_warshall
    from iterative.iterative_floyd import iterative_floyd


from sys import maxsize
NO_PATH = maxsize
GRAPH = [
    [0,   7,      NO_PATH, 8],
    [NO_PATH, 0,   5,       NO_PATH],
    [NO_PATH, NO_PATH, 0,    2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(GRAPH)  

def performance_test(function_handle):
    """
    A function that performs a simple performance test.
    function_handle -> The function which is being tested.
                       It must take no parameters.
    """

   
    test_graph = [row[:] for row in GRAPH]

    
    start_time = process_time()

    
    if function_handle == recursive_floyd_warshall:
        function_handle(0, 0, 0)  
    else:
        function_handle()  #

    
    end_time = process_time()
    print(f"{function_handle.__name__} Execution Time: {end_time - start_time:.6f} seconds")


print("🚀 Recursion Test Time")
performance_test(recursive_floyd_warshall)

print("\n🚀 Iterative Test Time")
performance_test(iterative_floyd)
