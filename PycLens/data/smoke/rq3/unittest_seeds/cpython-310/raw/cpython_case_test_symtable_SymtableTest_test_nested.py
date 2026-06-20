# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_nested

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.top.is_nested())
    self.assertFalse(self.Mine.is_nested())
    self.assertFalse(self.spam.is_nested())
    self.assertTrue(self.internal.is_nested())
