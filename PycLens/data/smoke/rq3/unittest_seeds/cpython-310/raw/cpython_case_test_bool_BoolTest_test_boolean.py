# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_boolean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(True & 1, 1)
    self.assertNotIsInstance(True & 1, bool)
    self.assertIs(True & True, True)
    self.assertEqual(True | 1, 1)
    self.assertNotIsInstance(True | 1, bool)
    self.assertIs(True | True, True)
    self.assertEqual(True ^ 1, 0)
    self.assertNotIsInstance(True ^ 1, bool)
    self.assertIs(True ^ True, False)
