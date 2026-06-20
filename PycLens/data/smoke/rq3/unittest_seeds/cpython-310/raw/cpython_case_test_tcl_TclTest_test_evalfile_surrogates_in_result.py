# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tcl.py
# case: TclTest_test_evalfile_surrogates_in_result

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tcl = self.interp
    encoding = tcl.call('encoding', 'system')
    self.addCleanup(tcl.call, 'encoding', 'system', encoding)
    tcl.call('encoding', 'system', 'utf-8')
    filename = os_helper.TESTFN_ASCII
    self.addCleanup(os_helper.unlink, filename)
    with open(filename, 'wb') as f:
        f.write(b'\n            set a "<\xed\xa0\xbd\xed\xb2\xbb>"\n            set b "<\\ud83d\\udcbb>"\n            ')
    tcl.evalfile(filename)
    self.assertEqual(tcl.eval('set a'), '<💻>')
    self.assertEqual(tcl.eval('set b'), '<💻>')
