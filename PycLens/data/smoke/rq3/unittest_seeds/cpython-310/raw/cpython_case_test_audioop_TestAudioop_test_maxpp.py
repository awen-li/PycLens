# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_maxpp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.maxpp(b'', w), 0)
        self.assertEqual(audioop.maxpp(bytearray(), w), 0)
        self.assertEqual(audioop.maxpp(memoryview(b''), w), 0)
        self.assertEqual(audioop.maxpp(packs[w](*range(100)), w), 0)
        self.assertEqual(audioop.maxpp(packs[w](9, 10, 5, 5, 0, 1), w), 10)
        self.assertEqual(audioop.maxpp(datas[w], w), maxvalues[w] - minvalues[w])
