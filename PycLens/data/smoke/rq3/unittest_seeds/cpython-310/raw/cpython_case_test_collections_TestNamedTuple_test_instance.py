# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    p = Point(11, 22)
    self.assertEqual(p, Point(x=11, y=22))
    self.assertEqual(p, Point(11, y=22))
    self.assertEqual(p, Point(y=22, x=11))
    self.assertEqual(p, Point(*(11, 22)))
    self.assertEqual(p, Point(**dict(x=11, y=22)))
    self.assertRaises(TypeError, Point, 1)
    self.assertRaises(TypeError, Point, 1, 2, 3)
    with self.assertRaises(TypeError):
        Point(XXX=1, y=2)
    with self.assertRaises(TypeError):
        Point(x=1)
    self.assertEqual(repr(p), 'Point(x=11, y=22)')
    self.assertNotIn('__weakref__', dir(p))
    self.assertEqual(p, Point._make([11, 22]))
    self.assertEqual(p._fields, ('x', 'y'))
    self.assertEqual(p._replace(x=1), (1, 22))
    self.assertEqual(p._asdict(), dict(x=11, y=22))
    try:
        p._replace(x=1, error=2)
    except ValueError:
        pass
    else:
        self._fail('Did not detect an incorrect fieldname')
    Point = namedtuple('Point', 'x, y')
    p = Point(x=11, y=22)
    self.assertEqual(repr(p), 'Point(x=11, y=22)')
    Point = namedtuple('Point', ('x', 'y'))
    p = Point(x=11, y=22)
    self.assertEqual(repr(p), 'Point(x=11, y=22)')
