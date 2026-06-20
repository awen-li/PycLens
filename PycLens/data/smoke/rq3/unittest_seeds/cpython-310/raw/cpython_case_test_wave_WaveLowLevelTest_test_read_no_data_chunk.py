# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wave.py
# case: WaveLowLevelTest_test_read_no_data_chunk

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'RIFF' + struct.pack('<L', 28) + b'WAVE'
    b += b'fmt ' + struct.pack('<LHHLLHH', 16, 1, 1, 11025, 11025, 1, 8)
    with self.assertRaisesRegex(wave.Error, 'fmt chunk and/or data chunk missing'):
        wave.open(io.BytesIO(b))
