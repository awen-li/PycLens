# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_class_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = dict[int, None]
    self.assertEqual(dict.fromkeys(range(2)), {0: None, 1: None})
    self.assertEqual(t.fromkeys(range(2)), {0: None, 1: None})
