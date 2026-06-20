# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_expr_bignum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp
    for i in self.get_integers():
        result = tcl.call('expr', str(i))
        if self.wantobjects:
            self.assertEqual(result, i)
            self.assertIsInstance(result, int)
        else:
            self.assertEqual(result, str(i))
            self.assertIsInstance(result, str)
    if get_tk_patchlevel() < (8, 5):
        self.assertRaises(TclError, tcl.call, 'expr', str(2 ** 1000))
