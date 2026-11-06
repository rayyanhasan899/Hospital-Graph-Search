"""Compare the supplied graph's search results with an independent exhaustive oracle."""
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from searchAlgos import a_star, gbfs, hospital_graph

def shortest(start, goal):
    found=[]
    def visit(node, seen, cost):
        if node==goal:
            found.append(cost)
            return
        for neighbor, weight in hospital_graph[node].items():
            if neighbor not in seen:
                visit(neighbor, seen | {neighbor}, cost + weight)
    visit(start, {start}, 0.0)
    return min(found) if found else None

class SearchTests(unittest.TestCase):
    def test_all_node_pairs(self):
        for start in hospital_graph:
            for goal in hospital_graph:
                with self.subTest(start=start,goal=goal):
                    expected=shortest(start,goal)
                    for algorithm in [a_star,gbfs]:
                        path,cost=algorithm(start,goal)
                        if expected is None:
                            self.assertIsNone(path)
                            self.assertIsNone(cost)
                        else:
                            self.assertEqual((path[0],path[-1]),(start,goal))
                            actual=sum(hospital_graph[a][b] for a,b in zip(path,path[1:]))
                            self.assertTrue(math.isclose(cost,actual))
                            if algorithm is a_star:
                                self.assertTrue(math.isclose(cost,expected))

if __name__=='__main__':
    unittest.main()
