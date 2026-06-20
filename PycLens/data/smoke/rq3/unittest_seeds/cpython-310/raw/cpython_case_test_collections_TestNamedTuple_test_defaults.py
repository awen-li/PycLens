# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Point = namedtuple('Point', 'x y', defaults=(10, 20))
    self.assertEqual(Point._field_defaults, {'x': 10, 'y': 20})
    self.assertEqual(Point(1, 2), (1, 2))
    self.assertEqual(Point(1), (1, 20))
    self.assertEqual(Point(), (10, 20))
    Point = namedtuple('Point', 'x y', defaults=(20,))
    self.assertEqual(Point._field_defaults, {'y': 20})
    self.assertEqual(Point(1, 2), (1, 2))
    self.assertEqual(Point(1), (1, 20))
    Point = namedtuple('Point', 'x y', defaults=())
    self.assertEqual(Point._field_defaults, {})
    self.assertEqual(Point(1, 2), (1, 2))
    with self.assertRaises(TypeError):
        Point(1)
    with self.assertRaises(TypeError):
        Point()
    with self.assertRaises(TypeError):
        Point(1, 2, 3)
    with self.assertRaises(TypeError):
        Point = namedtuple('Point', 'x y', defaults=(10, 20, 30))
    with self.assertRaises(TypeError):
        Point = namedtuple('Point', 'x y', defaults=10)
    with self.assertRaises(TypeError):
        Point = namedtuple('Point', 'x y', defaults=False)
    Point = namedtuple('Point', 'x y', defaults=None)
    self.assertEqual(Point._field_defaults, {})
    self.assertIsNone(Point.__new__.__defaults__, None)
    self.assertEqual(Point(10, 20), (10, 20))
    with self.assertRaises(TypeError):
        Point(10)
    Point = namedtuple('Point', 'x y', defaults=[10, 20])
    self.assertEqual(Point._field_defaults, {'x': 10, 'y': 20})
    self.assertEqual(Point.__new__.__defaults__, (10, 20))
    self.assertEqual(Point(1, 2), (1, 2))
    self.assertEqual(Point(1), (1, 20))
    self.assertEqual(Point(), (10, 20))
    Point = namedtuple('Point', 'x y', defaults=iter([10, 20]))
    self.assertEqual(Point._field_defaults, {'x': 10, 'y': 20})
    self.assertEqual(Point.__new__.__defaults__, (10, 20))
    self.assertEqual(Point(1, 2), (1, 2))
    self.assertEqual(Point(1), (1, 20))
    self.assertEqual(Point(), (10, 20))
