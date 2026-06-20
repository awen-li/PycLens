# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_minmax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.minmax(b'', w), (2147483647, -2147483648))
        self.assertEqual(audioop.minmax(bytearray(), w), (2147483647, -2147483648))
        self.assertEqual(audioop.minmax(memoryview(b''), w), (2147483647, -2147483648))
        p = packs[w]
        self.assertEqual(audioop.minmax(p(5), w), (5, 5))
        self.assertEqual(audioop.minmax(p(5, -8, -1), w), (-8, 5))
        self.assertEqual(audioop.minmax(p(maxvalues[w]), w), (maxvalues[w], maxvalues[w]))
        self.assertEqual(audioop.minmax(p(minvalues[w]), w), (minvalues[w], minvalues[w]))
        self.assertEqual(audioop.minmax(datas[w], w), (minvalues[w], maxvalues[w]))
