# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_write_markers_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fout = aifc.open(io.BytesIO(), 'wb')
    self.assertRaises(aifc.Error, fout.setmark, 0, 0, b'')
    self.assertRaises(aifc.Error, fout.setmark, 1, -1, b'')
    self.assertRaises(aifc.Error, fout.setmark, 1, 0, None)
    self.assertRaises(aifc.Error, fout.getmark, 1)
    fout.initfp(None)
