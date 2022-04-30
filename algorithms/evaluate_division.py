"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
"""
from typing import List, Tuple, Dict

def make_graph(
        equations: List[List[str]],
        values: List[float],
        ) -> Dict[Tuple[str, str], float]:
    n = len(equations)
    graph = {tuple(equations[i]): values[i]
            for i in range(n)}
    for i in range(n):
        graph[(equations[i][1], equations[i][0])] = 1.0 / values[i]
    to_add = [(pair, value) for pair, value in graph.items()]
    while len(to_add) > 0:
        pair, val = to_add.pop()
        new_graph = {}
        for key, node in graph.items():
            if ((key[1] == pair[0]) or (key[0] == pair[1])):
                if key[1] == pair[0]:
                    new_pair = (key[0], pair[1])
                else:
                    new_pair = (pair[0], key[1])
                new_pair_t = (new_pair[1], new_pair[0])
                new_val = val * node
                if new_pair not in graph:
                    new_graph[new_pair] = new_val
                    to_add.append((new_pair, new_val))
                    new_graph[new_pair_t] = 1.0 / new_val
                    #to_add.append((new_pair_t, 1.0 / new_val))
        graph.update(new_graph)
    return graph

def evaluate_division(
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
        ) -> List[float]:
    graph = make_graph(equations, values)
    ret = [graph[tuple(x)]
           if tuple(x) in graph else -1.0
           for x in queries]
    return ret

