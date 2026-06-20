# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_wrongsize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'abcdefgh'
    state = None
    for size in (-1, 0, 5, 1024):
        self.assertRaises(audioop.error, audioop.ulaw2lin, data, size)
        self.assertRaises(audioop.error, audioop.alaw2lin, data, size)
        self.assertRaises(audioop.error, audioop.adpcm2lin, data, size, state)
