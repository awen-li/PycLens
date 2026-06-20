# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    p = Point(11, 22)
    with self.assertRaises(AttributeError):
        p.x = 33
    with self.assertRaises(AttributeError):
        del p.x
    with self.assertRaises(TypeError):
        p[0] = 33
    with self.assertRaises(TypeError):
        del p[0]
    self.assertEqual(p.x, 11)
    self.assertEqual(p[0], 11)
