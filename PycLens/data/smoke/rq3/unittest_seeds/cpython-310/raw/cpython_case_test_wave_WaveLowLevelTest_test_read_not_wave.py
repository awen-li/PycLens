# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wave.py
# case: WaveLowLevelTest_test_read_not_wave

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'RIFF' + struct.pack('<L', 4) + b'SPAM'
    with self.assertRaisesRegex(wave.Error, 'not a WAVE file'):
        wave.open(io.BytesIO(b))
