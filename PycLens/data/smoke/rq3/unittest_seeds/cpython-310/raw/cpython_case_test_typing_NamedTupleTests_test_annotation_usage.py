# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_annotation_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tim = CoolEmployee('Tim', 9000)
    self.assertIsInstance(tim, CoolEmployee)
    self.assertIsInstance(tim, tuple)
    self.assertEqual(tim.name, 'Tim')
    self.assertEqual(tim.cool, 9000)
    self.assertEqual(CoolEmployee.__name__, 'CoolEmployee')
    self.assertEqual(CoolEmployee._fields, ('name', 'cool'))
    self.assertEqual(CoolEmployee.__annotations__, collections.OrderedDict(name=str, cool=int))
