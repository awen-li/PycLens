# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_field_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y')
    p = Point(11, 22)
    self.assertTrue(inspect.isdatadescriptor(Point.x))
    self.assertEqual(Point.x.__get__(p), 11)
    self.assertRaises(AttributeError, Point.x.__set__, p, 33)
    self.assertRaises(AttributeError, Point.x.__delete__, p)

    class NewPoint(tuple):
        x = pickle.loads(pickle.dumps(Point.x))
        y = pickle.loads(pickle.dumps(Point.y))
    np = NewPoint([1, 2])
    self.assertEqual(np.x, 1)
    self.assertEqual(np.y, 2)
