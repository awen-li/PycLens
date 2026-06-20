# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AifcMiscTest_test_read_markers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fout = self.fout = aifc.open(TESTFN, 'wb')
    fout.aiff()
    fout.setparams((1, 1, 1, 1, b'NONE', b''))
    fout.setmark(1, 0, b'odd')
    fout.setmark(2, 0, b'even')
    fout.writeframes(b'\x00')
    fout.close()
    f = aifc.open(TESTFN, 'rb')
    self.addCleanup(f.close)
    self.assertEqual(f.getmarkers(), [(1, 0, b'odd'), (2, 0, b'even')])
    self.assertEqual(f.getmark(1), (1, 0, b'odd'))
    self.assertEqual(f.getmark(2), (2, 0, b'even'))
    self.assertRaises(aifc.Error, f.getmark, 3)
