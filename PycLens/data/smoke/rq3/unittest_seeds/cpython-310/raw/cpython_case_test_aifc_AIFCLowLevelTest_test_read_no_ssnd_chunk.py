# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_no_ssnd_chunk

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
    b += b'COMM' + struct.pack('>LhlhhLL', 38, 1, 0, 8, 16384 | 12, 11025 << 18, 0)
    b += b'NONE' + struct.pack('B', 14) + b'not compressed' + b'\x00'
    with self.assertRaisesRegex(aifc.Error, 'COMM chunk and/or SSND chunk missing'):
        aifc.open(io.BytesIO(b))
