# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AifcMiscTest_test_params_added

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.f = aifc.open(TESTFN, 'wb')
    f.aiff()
    f.setparams((1, 1, 1, 1, b'NONE', b''))
    f.close()
    f = aifc.open(TESTFN, 'rb')
    self.addCleanup(f.close)
    params = f.getparams()
    self.assertEqual(params.nchannels, f.getnchannels())
    self.assertEqual(params.sampwidth, f.getsampwidth())
    self.assertEqual(params.framerate, f.getframerate())
    self.assertEqual(params.nframes, f.getnframes())
    self.assertEqual(params.comptype, f.getcomptype())
    self.assertEqual(params.compname, f.getcompname())
