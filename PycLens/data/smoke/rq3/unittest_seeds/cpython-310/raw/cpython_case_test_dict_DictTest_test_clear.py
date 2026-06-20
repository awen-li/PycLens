# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {1: 1, 2: 2, 3: 3}
    d.clear()
    self.assertEqual(d, {})
    self.assertRaises(TypeError, d.clear, None)
