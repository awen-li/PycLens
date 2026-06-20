# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: BigmemTclTest_test_huge_string_builtins2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tk = self.interp.tk
    value = '1' + ' ' * size
    self.assertRaises(OverflowError, tk.evalfile, value)
    self.assertRaises(OverflowError, tk.unsetvar, value)
    self.assertRaises(OverflowError, tk.unsetvar, 'x', value)
