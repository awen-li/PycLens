# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(complex(False), 0j)
    self.assertEqual(complex(False), False)
    self.assertEqual(complex(True), 1 + 0j)
    self.assertEqual(complex(True), True)
