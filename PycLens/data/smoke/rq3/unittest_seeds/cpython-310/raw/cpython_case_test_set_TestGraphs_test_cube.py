# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestGraphs_test_cube

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = cube(3)
    vertices1 = set(g)
    self.assertEqual(len(vertices1), 8)
    for edge in g.values():
        self.assertEqual(len(edge), 3)
    vertices2 = set((v for edges in g.values() for v in edges))
    self.assertEqual(vertices1, vertices2)
    cubefaces = faces(g)
    self.assertEqual(len(cubefaces), 6)
    for face in cubefaces:
        self.assertEqual(len(face), 4)
