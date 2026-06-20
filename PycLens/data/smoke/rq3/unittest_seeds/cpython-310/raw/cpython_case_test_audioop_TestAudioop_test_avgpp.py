# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_avgpp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.avgpp(b'', w), 0)
        self.assertEqual(audioop.avgpp(bytearray(), w), 0)
        self.assertEqual(audioop.avgpp(memoryview(b''), w), 0)
        self.assertEqual(audioop.avgpp(packs[w](*range(100)), w), 0)
        self.assertEqual(audioop.avgpp(packs[w](9, 10, 5, 5, 0, 1), w), 10)
    self.assertEqual(audioop.avgpp(datas[1], 1), 196)
    self.assertEqual(audioop.avgpp(datas[2], 2), 50534)
    self.assertEqual(audioop.avgpp(datas[3], 3), 12937096)
    self.assertEqual(audioop.avgpp(datas[4], 4), 3311897002)
