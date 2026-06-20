# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_id

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertGreater(self.top.get_id(), 0)
    self.assertGreater(self.Mine.get_id(), 0)
    self.assertGreater(self.a_method.get_id(), 0)
    self.assertGreater(self.spam.get_id(), 0)
    self.assertGreater(self.internal.get_id(), 0)
