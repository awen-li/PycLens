# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_py36_class_syntax_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(LabelPoint2D.__name__, 'LabelPoint2D')
    self.assertEqual(LabelPoint2D.__module__, __name__)
    self.assertEqual(LabelPoint2D.__annotations__, {'x': int, 'y': int, 'label': str})
    self.assertEqual(LabelPoint2D.__bases__, (dict,))
    self.assertEqual(LabelPoint2D.__total__, True)
    self.assertNotIsSubclass(LabelPoint2D, typing.Sequence)
    not_origin = Point2D(x=0, y=1)
    self.assertEqual(not_origin['x'], 0)
    self.assertEqual(not_origin['y'], 1)
    other = LabelPoint2D(x=0, y=1, label='hi')
    self.assertEqual(other['label'], 'hi')
