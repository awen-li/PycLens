# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_invalid_adpcm_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, audioop.adpcm2lin, b'\x00', 1, 555)
    self.assertRaises(TypeError, audioop.lin2adpcm, b'\x00', 1, 555)
    self.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (0, -1))
    self.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (0, 89))
    self.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (0, -1))
    self.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (0, 89))
    self.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (-32769, 0))
    self.assertRaises(ValueError, audioop.adpcm2lin, b'\x00', 1, (32768, 0))
    self.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (-32769, 0))
    self.assertRaises(ValueError, audioop.lin2adpcm, b'\x00', 1, (32768, 0))
