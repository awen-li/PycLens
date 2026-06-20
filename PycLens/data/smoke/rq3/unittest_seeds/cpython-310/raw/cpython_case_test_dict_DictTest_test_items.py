# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    self.assertEqual(set(d.items()), set())
    d = {1: 2}
    self.assertEqual(set(d.items()), {(1, 2)})
    self.assertRaises(TypeError, d.items, None)
    self.assertEqual(repr(dict(a=1).items()), "dict_items([('a', 1)])")
