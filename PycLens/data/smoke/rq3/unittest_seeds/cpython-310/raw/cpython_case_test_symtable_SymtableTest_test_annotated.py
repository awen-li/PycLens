# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_annotated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    st1 = symtable.symtable('def f():\n    x: int\n', 'test', 'exec')
    st2 = st1.get_children()[0]
    self.assertTrue(st2.lookup('x').is_local())
    self.assertTrue(st2.lookup('x').is_annotated())
    self.assertFalse(st2.lookup('x').is_global())
    st3 = symtable.symtable('def f():\n    x = 1\n', 'test', 'exec')
    st4 = st3.get_children()[0]
    self.assertTrue(st4.lookup('x').is_local())
    self.assertFalse(st4.lookup('x').is_annotated())
    st5 = symtable.symtable('global x\nx: int', 'test', 'exec')
    self.assertTrue(st5.lookup('x').is_global())
    st6 = symtable.symtable('def g():\n    x = 2\n    def f():\n        nonlocal x\n    x: int', 'test', 'exec')
