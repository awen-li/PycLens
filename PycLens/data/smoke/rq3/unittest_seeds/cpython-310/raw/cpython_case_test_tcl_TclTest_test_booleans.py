# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_booleans

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp

    def check(expr, expected):
        result = tcl.call('expr', expr)
        if tcl.wantobjects():
            self.assertEqual(result, expected)
            self.assertIsInstance(result, int)
        else:
            self.assertIn(result, (expr, str(int(expected))))
            self.assertIsInstance(result, str)
    check('true', True)
    check('yes', True)
    check('on', True)
    check('false', False)
    check('no', False)
    check('off', False)
    check('1 < 2', True)
    check('1 > 2', False)
