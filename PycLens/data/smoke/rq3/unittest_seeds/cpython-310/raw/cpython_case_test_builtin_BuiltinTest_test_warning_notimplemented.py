# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_warning_notimplemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertWarns(DeprecationWarning, bool, NotImplemented)
    with self.assertWarns(DeprecationWarning):
        self.assertTrue(NotImplemented)
    with self.assertWarns(DeprecationWarning):
        self.assertFalse(not NotImplemented)
