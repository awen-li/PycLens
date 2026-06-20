# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestGraphs_test_cuboctahedron

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = cube(3)
    cuboctahedron = linegraph(g)
    self.assertEqual(len(cuboctahedron), 12)
    vertices = set(cuboctahedron)
    for edges in cuboctahedron.values():
        self.assertEqual(len(edges), 4)
    othervertices = set((edge for edges in cuboctahedron.values() for edge in edges))
    self.assertEqual(vertices, othervertices)
    cubofaces = faces(cuboctahedron)
    facesizes = collections.defaultdict(int)
    for face in cubofaces:
        facesizes[len(face)] += 1
    self.assertEqual(facesizes[3], 8)
    self.assertEqual(facesizes[4], 6)
    for vertex in cuboctahedron:
        edge = vertex
        self.assertEqual(len(edge), 2)
        for cubevert in edge:
            self.assertIn(cubevert, g)
