# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_avg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.avg(b'', w), 0)
        self.assertEqual(audioop.avg(bytearray(), w), 0)
        self.assertEqual(audioop.avg(memoryview(b''), w), 0)
        p = packs[w]
        self.assertEqual(audioop.avg(p(5), w), 5)
        self.assertEqual(audioop.avg(p(5, 8), w), 6)
        self.assertEqual(audioop.avg(p(5, -8), w), -2)
        self.assertEqual(audioop.avg(p(maxvalues[w], maxvalues[w]), w), maxvalues[w])
        self.assertEqual(audioop.avg(p(minvalues[w], minvalues[w]), w), minvalues[w])
    self.assertEqual(audioop.avg(packs[4](1342177280, 1879048192), 4), 1610612736)
    self.assertEqual(audioop.avg(packs[4](-1342177280, -1879048192), 4), -1610612736)
