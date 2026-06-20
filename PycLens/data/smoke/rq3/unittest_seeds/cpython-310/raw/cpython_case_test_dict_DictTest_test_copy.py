# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 1, 2: 2, 3: 3}
    self.assertIsNot(d.copy(), d)
    self.assertEqual(d.copy(), d)
    self.assertEqual(d.copy(), {1: 1, 2: 2, 3: 3})
    copy = d.copy()
    d[4] = 4
    self.assertNotEqual(copy, d)
    self.assertEqual({}.copy(), {})
    self.assertRaises(TypeError, d.copy, None)
