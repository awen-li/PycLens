# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_rms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.rms(b'', w), 0)
        self.assertEqual(audioop.rms(bytearray(), w), 0)
        self.assertEqual(audioop.rms(memoryview(b''), w), 0)
        p = packs[w]
        self.assertEqual(audioop.rms(p(*range(100)), w), 57)
        self.assertAlmostEqual(audioop.rms(p(maxvalues[w]) * 5, w), maxvalues[w], delta=1)
        self.assertAlmostEqual(audioop.rms(p(minvalues[w]) * 5, w), -minvalues[w], delta=1)
    self.assertEqual(audioop.rms(datas[1], 1), 77)
    self.assertEqual(audioop.rms(datas[2], 2), 20001)
    self.assertEqual(audioop.rms(datas[3], 3), 5120523)
    self.assertEqual(audioop.rms(datas[4], 4), 1310854152)
