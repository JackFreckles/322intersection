'''
Clinton Reimann
CSCI 332 Spring 2025
Programming Assignment #class17 (tests)

I acknowledge that I have worked on this assignment independently, except
where explicitly noted and referenced. Any collaboration or use of external
resources has been properly cited. I am fully aware of the consequences of
academic dishonesty and agree to abide by the university's academic integrity
policy. I understand the importance the consequences of plagiarism.
'''

import unittest
from main import do_intersect

class TestIntersections(unittest.TestCase):
    def test_colinear_no_intersection(self):
        p1 = (1.0, 1.0)
        p2 = (4.0, 4.0)
        p3 = (2.0, 1.0)
        p4 = (5.0, 4.0)
        seg1 = (p1, p2)
        seg2 = (p3, p4)
        self.assertEqual(do_intersect(seg1, seg2), False)
        
    def test_colinear_all_intersection(self):
        seg1 = ((1.0, 1.0), (4.0, 4.0))
        seg2 = ((1.0, 1.0), (4.0, 4.0))
        self.assertEqual(do_intersect(seg1, seg2), True)
        
    def test_nonlinear_no_intersect(self):
        seg1 = ((1.0, 1.0), (4.0, 4.0))
        seg2 = ((1.0, 2.0), (-1.0, 4.0))
        self.assertEqual(do_intersect(seg1, seg2), False)
        
    def test_nonlinear_intersect(self):
        seg1 = ((1.0, 1.0), (4.0, 4.0))
        seg2 = ((1.0, 2.0), (5.0, 4.0))
        self.assertEqual(do_intersect(seg1, seg2), True)
        
    def test_colinear_partial_overlap(self):
        seg1 = ((1.0, 1.0), (4.0, 4.0))
        seg2 = ((2.0, 2.0), (6.0, 6.0))
        self.assertEqual(do_intersect(seg1, seg2), True)
        
    def test_colinear_touching_endpoint(self):
        seg1 = ((1.0, 1.0), (4.0, 4.0))
        seg2 = ((4.0, 4.0), (6.0, 6.0))
        self.assertEqual(do_intersect(seg1, seg2), True)
        
    def test_nonlinear_touching(self):
        seg1 = ((1.0, 1.0), (4.0, 4.0))
        seg2 = ((4.0, 4.0), (6.0, 2.0))
        self.assertEqual(do_intersect(seg1, seg2), True)
        
    def test_vertical_intersection(self):
        seg1 = ((2.0, 1.0), (2.0, 5.0))
        seg2 = ((0.0, 3.0), (4.0, 3.0))
        self.assertEqual(do_intersect(seg1, seg2), True)

if __name__ == "__main__":
    unittest.main()