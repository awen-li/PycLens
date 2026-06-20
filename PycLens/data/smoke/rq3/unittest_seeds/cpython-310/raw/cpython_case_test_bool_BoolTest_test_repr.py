# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(False), 'False')
    self.assertEqual(repr(True), 'True')
    self.assertIs(eval(repr(False)), False)
    self.assertIs(eval(repr(True)), True)
