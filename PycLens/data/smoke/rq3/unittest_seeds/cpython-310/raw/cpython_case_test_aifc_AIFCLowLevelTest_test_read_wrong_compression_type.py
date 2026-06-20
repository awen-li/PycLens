# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_wrong_compression_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
    b += b'COMM' + struct.pack('>LhlhhLL', 23, 1, 0, 8, 16384 | 12, 11025 << 18, 0)
    b += b'WRNG' + struct.pack('B', 0)
    self.assertRaises(aifc.Error, aifc.open, io.BytesIO(b))
