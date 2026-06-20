# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_cross

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.cross(b'', w), -1)
        self.assertEqual(audioop.cross(bytearray(), w), -1)
        self.assertEqual(audioop.cross(memoryview(b''), w), -1)
        p = packs[w]
        self.assertEqual(audioop.cross(p(0, 1, 2), w), 0)
        self.assertEqual(audioop.cross(p(1, 2, -3, -4), w), 1)
        self.assertEqual(audioop.cross(p(-1, -2, 3, 4), w), 1)
        self.assertEqual(audioop.cross(p(0, minvalues[w]), w), 1)
        self.assertEqual(audioop.cross(p(minvalues[w], maxvalues[w]), w), 1)
