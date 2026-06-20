# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_max

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.max(b'', w), 0)
        self.assertEqual(audioop.max(bytearray(), w), 0)
        self.assertEqual(audioop.max(memoryview(b''), w), 0)
        p = packs[w]
        self.assertEqual(audioop.max(p(5), w), 5)
        self.assertEqual(audioop.max(p(5, -8, -1), w), 8)
        self.assertEqual(audioop.max(p(maxvalues[w]), w), maxvalues[w])
        self.assertEqual(audioop.max(p(minvalues[w]), w), -minvalues[w])
        self.assertEqual(audioop.max(datas[w], w), -minvalues[w])
