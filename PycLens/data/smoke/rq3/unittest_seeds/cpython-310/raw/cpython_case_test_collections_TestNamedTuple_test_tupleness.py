# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_tupleness

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    p = Point(11, 22)
    self.assertIsInstance(p, tuple)
    self.assertEqual(p, (11, 22))
    self.assertEqual(tuple(p), (11, 22))
    self.assertEqual(list(p), [11, 22])
    self.assertEqual(max(p), 22)
    self.assertEqual(max(*p), 22)
    (x, y) = p
    self.assertEqual(p, (x, y))
    self.assertEqual((p[0], p[1]), (11, 22))
    with self.assertRaises(IndexError):
        p[3]
    self.assertEqual(p[-1], 22)
    self.assertEqual(hash(p), hash((11, 22)))
    self.assertEqual(p.x, x)
    self.assertEqual(p.y, y)
    with self.assertRaises(AttributeError):
        p.z
