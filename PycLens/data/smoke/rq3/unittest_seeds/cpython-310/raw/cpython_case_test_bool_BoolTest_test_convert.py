# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_convert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, bool, 42, 42)
    self.assertIs(bool(10), True)
    self.assertIs(bool(1), True)
    self.assertIs(bool(-1), True)
    self.assertIs(bool(0), False)
    self.assertIs(bool('hello'), True)
    self.assertIs(bool(''), False)
    self.assertIs(bool(), False)
