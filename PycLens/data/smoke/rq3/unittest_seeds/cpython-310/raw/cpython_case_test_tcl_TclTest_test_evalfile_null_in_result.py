# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_evalfile_null_in_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp
    filename = os_helper.TESTFN_ASCII
    self.addCleanup(os_helper.unlink, filename)
    with open(filename, 'w') as f:
        f.write('\n            set a "a\x00b"\n            set b "a\\0b"\n            ')
    tcl.evalfile(filename)
    self.assertEqual(tcl.eval('set a'), 'a\x00b')
    self.assertEqual(tcl.eval('set b'), 'a\x00b')
