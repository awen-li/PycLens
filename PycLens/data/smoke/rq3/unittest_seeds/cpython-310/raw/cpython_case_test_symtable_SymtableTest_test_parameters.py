# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sym in ('a', 'var', 'kw'):
        self.assertTrue(self.spam.lookup(sym).is_parameter())
    self.assertFalse(self.spam.lookup('x').is_parameter())
