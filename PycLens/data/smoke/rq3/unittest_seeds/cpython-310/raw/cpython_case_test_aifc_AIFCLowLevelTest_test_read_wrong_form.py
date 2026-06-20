# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_wrong_form

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b1 = io.BytesIO(b'WRNG' + struct.pack('>L', 0))
    b2 = io.BytesIO(b'FORM' + struct.pack('>L', 4) + b'WRNG')
    self.assertRaises(aifc.Error, aifc.open, b1)
    self.assertRaises(aifc.Error, aifc.open, b2)
