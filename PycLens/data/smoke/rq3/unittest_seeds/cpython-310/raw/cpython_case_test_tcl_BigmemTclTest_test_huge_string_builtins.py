# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: BigmemTclTest_test_huge_string_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tk = self.interp.tk
    value = '1' + ' ' * size
    self.assertRaises(OverflowError, tk.getint, value)
    self.assertRaises(OverflowError, tk.getdouble, value)
    self.assertRaises(OverflowError, tk.getboolean, value)
    self.assertRaises(OverflowError, tk.eval, value)
    self.assertRaises(OverflowError, tk.evalfile, value)
    self.assertRaises(OverflowError, tk.record, value)
    self.assertRaises(OverflowError, tk.adderrorinfo, value)
    self.assertRaises(OverflowError, tk.setvar, value, 'x', 'a')
    self.assertRaises(OverflowError, tk.setvar, 'x', value, 'a')
    self.assertRaises(OverflowError, tk.unsetvar, value)
    self.assertRaises(OverflowError, tk.unsetvar, 'x', value)
    self.assertRaises(OverflowError, tk.adderrorinfo, value)
    self.assertRaises(OverflowError, tk.exprstring, value)
    self.assertRaises(OverflowError, tk.exprlong, value)
    self.assertRaises(OverflowError, tk.exprboolean, value)
    self.assertRaises(OverflowError, tk.splitlist, value)
    self.assertRaises(OverflowError, tk.split, value)
    self.assertRaises(OverflowError, tk.createcommand, value, max)
    self.assertRaises(OverflowError, tk.deletecommand, value)
