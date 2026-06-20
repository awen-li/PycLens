# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'abcd'
    size = 2
    self.assertRaises(TypeError, audioop.getsample, data, size, 0)
    self.assertRaises(TypeError, audioop.max, data, size)
    self.assertRaises(TypeError, audioop.minmax, data, size)
    self.assertRaises(TypeError, audioop.avg, data, size)
    self.assertRaises(TypeError, audioop.rms, data, size)
    self.assertRaises(TypeError, audioop.avgpp, data, size)
    self.assertRaises(TypeError, audioop.maxpp, data, size)
    self.assertRaises(TypeError, audioop.cross, data, size)
    self.assertRaises(TypeError, audioop.mul, data, size, 1.0)
    self.assertRaises(TypeError, audioop.tomono, data, size, 0.5, 0.5)
    self.assertRaises(TypeError, audioop.tostereo, data, size, 0.5, 0.5)
    self.assertRaises(TypeError, audioop.add, data, data, size)
    self.assertRaises(TypeError, audioop.bias, data, size, 0)
    self.assertRaises(TypeError, audioop.reverse, data, size)
    self.assertRaises(TypeError, audioop.lin2lin, data, size, size)
    self.assertRaises(TypeError, audioop.ratecv, data, size, 1, 1, 1, None)
    self.assertRaises(TypeError, audioop.lin2ulaw, data, size)
    self.assertRaises(TypeError, audioop.lin2alaw, data, size)
    self.assertRaises(TypeError, audioop.lin2adpcm, data, size, None)
