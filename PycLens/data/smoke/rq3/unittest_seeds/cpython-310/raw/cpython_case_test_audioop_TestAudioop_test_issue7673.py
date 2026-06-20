# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_issue7673

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = None
    for (data, size) in INVALID_DATA:
        size2 = size
        self.assertRaises(audioop.error, audioop.getsample, data, size, 0)
        self.assertRaises(audioop.error, audioop.max, data, size)
        self.assertRaises(audioop.error, audioop.minmax, data, size)
        self.assertRaises(audioop.error, audioop.avg, data, size)
        self.assertRaises(audioop.error, audioop.rms, data, size)
        self.assertRaises(audioop.error, audioop.avgpp, data, size)
        self.assertRaises(audioop.error, audioop.maxpp, data, size)
        self.assertRaises(audioop.error, audioop.cross, data, size)
        self.assertRaises(audioop.error, audioop.mul, data, size, 1.0)
        self.assertRaises(audioop.error, audioop.tomono, data, size, 0.5, 0.5)
        self.assertRaises(audioop.error, audioop.tostereo, data, size, 0.5, 0.5)
        self.assertRaises(audioop.error, audioop.add, data, data, size)
        self.assertRaises(audioop.error, audioop.bias, data, size, 0)
        self.assertRaises(audioop.error, audioop.reverse, data, size)
        self.assertRaises(audioop.error, audioop.lin2lin, data, size, size2)
        self.assertRaises(audioop.error, audioop.ratecv, data, size, 1, 1, 1, state)
        self.assertRaises(audioop.error, audioop.lin2ulaw, data, size)
        self.assertRaises(audioop.error, audioop.lin2alaw, data, size)
        self.assertRaises(audioop.error, audioop.lin2adpcm, data, size, state)
