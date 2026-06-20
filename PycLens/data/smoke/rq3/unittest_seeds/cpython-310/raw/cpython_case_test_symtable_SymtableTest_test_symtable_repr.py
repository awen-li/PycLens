# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_symtable_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(self.top), '<SymbolTable for module ?>')
    self.assertEqual(str(self.spam), '<Function SymbolTable for spam in ?>')
