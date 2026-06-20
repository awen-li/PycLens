# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_field_doc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    self.assertEqual(Point.x.__doc__, 'Alias for field number 0')
    self.assertEqual(Point.y.__doc__, 'Alias for field number 1')
    Point.x.__doc__ = 'docstring for Point.x'
    self.assertEqual(Point.x.__doc__, 'docstring for Point.x')
    Vector = namedtuple('Vector', 'x y')
    self.assertEqual(Vector.x.__doc__, 'Alias for field number 0')
    Vector.x.__doc__ = 'docstring for Vector.x'
    self.assertEqual(Vector.x.__doc__, 'docstring for Vector.x')
