# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_byteswap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    swapped_datas = {1: datas[1], 2: packs[2](0, 13330, 26437, -26182, -129, 128, -1), 3: packs[3](0, 5649426, -7772347, 7837882, -129, 128, -1), 4: packs[4](0, 2018915346, -1417058491, 1433835706, -129, 128, -1)}
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.byteswap(b'', w), b'')
        self.assertEqual(audioop.byteswap(datas[w], w), swapped_datas[w])
        self.assertEqual(audioop.byteswap(swapped_datas[w], w), datas[w])
        self.assertEqual(audioop.byteswap(bytearray(datas[w]), w), swapped_datas[w])
        self.assertEqual(audioop.byteswap(memoryview(datas[w]), w), swapped_datas[w])
