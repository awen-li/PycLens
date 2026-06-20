# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    self.assertEqual(Point.__name__, 'Point')
    self.assertEqual(Point.__slots__, ())
    self.assertEqual(Point.__module__, __name__)
    self.assertEqual(Point.__getitem__, tuple.__getitem__)
    self.assertEqual(Point._fields, ('x', 'y'))
    self.assertRaises(ValueError, namedtuple, 'abc%', 'efg ghi')
    self.assertRaises(ValueError, namedtuple, 'class', 'efg ghi')
    self.assertRaises(ValueError, namedtuple, '9abc', 'efg ghi')
    self.assertRaises(ValueError, namedtuple, 'abc', 'efg g%hi')
    self.assertRaises(ValueError, namedtuple, 'abc', 'abc class')
    self.assertRaises(ValueError, namedtuple, 'abc', '8efg 9ghi')
    self.assertRaises(ValueError, namedtuple, 'abc', '_efg ghi')
    self.assertRaises(ValueError, namedtuple, 'abc', 'efg efg ghi')
    namedtuple('Point0', 'x1 y2')
    namedtuple('_', 'a b c')
    nt = namedtuple('nt', 'the quick brown fox')
    self.assertNotIn("u'", repr(nt._fields))
    nt = namedtuple('nt', ('the', 'quick'))
    self.assertNotIn("u'", repr(nt._fields))
    self.assertRaises(TypeError, Point._make, [11])
    self.assertRaises(TypeError, Point._make, [11, 22, 33])
