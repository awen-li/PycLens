# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wave.py
# case: WaveLowLevelTest_test_read_wrong_number_of_channels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'RIFF' + struct.pack('<L', 36) + b'WAVE'
    b += b'fmt ' + struct.pack('<LHHLLHH', 16, 1, 0, 11025, 11025, 1, 8)
    b += b'data' + struct.pack('<L', 0)
    with self.assertRaisesRegex(wave.Error, 'bad # of channels'):
        wave.open(io.BytesIO(b))
