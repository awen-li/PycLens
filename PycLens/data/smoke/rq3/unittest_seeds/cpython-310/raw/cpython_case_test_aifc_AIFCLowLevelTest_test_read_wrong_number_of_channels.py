# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_wrong_number_of_channels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for nchannels in (0, -1):
        b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
        b += b'COMM' + struct.pack('>LhlhhLL', 38, nchannels, 0, 8, 16384 | 12, 11025 << 18, 0)
        b += b'NONE' + struct.pack('B', 14) + b'not compressed' + b'\x00'
        b += b'SSND' + struct.pack('>L', 8) + b'\x00' * 8
        with self.assertRaisesRegex(aifc.Error, 'bad # of channels'):
            aifc.open(io.BytesIO(b))
