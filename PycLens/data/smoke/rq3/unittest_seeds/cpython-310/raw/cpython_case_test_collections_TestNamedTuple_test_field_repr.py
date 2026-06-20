# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_field_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    self.assertEqual(repr(Point.x), "_tuplegetter(0, 'Alias for field number 0')")
    self.assertEqual(repr(Point.y), "_tuplegetter(1, 'Alias for field number 1')")
    Point.x.__doc__ = 'The x-coordinate'
    Point.y.__doc__ = 'The y-coordinate'
    self.assertEqual(repr(Point.x), "_tuplegetter(0, 'The x-coordinate')")
    self.assertEqual(repr(Point.y), "_tuplegetter(1, 'The y-coordinate')")
