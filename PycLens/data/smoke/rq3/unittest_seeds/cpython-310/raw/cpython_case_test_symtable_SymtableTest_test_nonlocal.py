# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_nonlocal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.spam.lookup('some_var').is_nonlocal())
    self.assertTrue(self.other_internal.lookup('some_var').is_nonlocal())
    expected = ('some_var',)
    self.assertEqual(self.other_internal.get_nonlocals(), expected)
