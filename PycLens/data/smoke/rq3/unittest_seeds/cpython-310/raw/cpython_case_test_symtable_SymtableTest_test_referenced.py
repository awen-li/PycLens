# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_referenced

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.internal.lookup('x').is_referenced())
    self.assertTrue(self.spam.lookup('internal').is_referenced())
    self.assertFalse(self.spam.lookup('x').is_referenced())
