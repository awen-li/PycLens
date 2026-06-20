# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_lin2adpcm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.lin2adpcm(datas[1], 1, None), (b'\x07\x7f\x7f', (-221, 39)))
    self.assertEqual(audioop.lin2adpcm(bytearray(datas[1]), 1, None), (b'\x07\x7f\x7f', (-221, 39)))
    self.assertEqual(audioop.lin2adpcm(memoryview(datas[1]), 1, None), (b'\x07\x7f\x7f', (-221, 39)))
    for w in (2, 3, 4):
        self.assertEqual(audioop.lin2adpcm(datas[w], w, None), (b'\x07\x7f\x7f', (31, 39)))
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.lin2adpcm(b'\x00' * w * 10, w, None), (b'\x00' * 5, (0, 0)))
