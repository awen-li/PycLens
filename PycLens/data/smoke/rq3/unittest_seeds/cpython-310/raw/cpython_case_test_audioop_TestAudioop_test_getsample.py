# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_getsample

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        data = packs[w](0, 1, -1, maxvalues[w], minvalues[w])
        self.assertEqual(audioop.getsample(data, w, 0), 0)
        self.assertEqual(audioop.getsample(bytearray(data), w, 0), 0)
        self.assertEqual(audioop.getsample(memoryview(data), w, 0), 0)
        self.assertEqual(audioop.getsample(data, w, 1), 1)
        self.assertEqual(audioop.getsample(data, w, 2), -1)
        self.assertEqual(audioop.getsample(data, w, 3), maxvalues[w])
        self.assertEqual(audioop.getsample(data, w, 4), minvalues[w])
