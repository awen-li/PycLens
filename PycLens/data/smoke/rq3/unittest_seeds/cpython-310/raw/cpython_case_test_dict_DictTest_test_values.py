# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertEqual(set(d.values()), set())
    d = {1: 2}
    self.assertEqual(set(d.values()), {2})
    self.assertRaises(TypeError, d.values, None)
    self.assertEqual(repr(dict(a=1).values()), 'dict_values([1])')
