# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_symtable.py
# case: SymtableTest_test_function_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    func = self.spam
    self.assertEqual(sorted(func.get_parameters()), ['a', 'b', 'kw', 'var'])
    expected = ['a', 'b', 'internal', 'kw', 'other_internal', 'some_var', 'var', 'x']
    self.assertEqual(sorted(func.get_locals()), expected)
    self.assertEqual(sorted(func.get_globals()), ['bar', 'glob', 'some_assigned_global_var'])
    self.assertEqual(self.internal.get_frees(), ('x',))
