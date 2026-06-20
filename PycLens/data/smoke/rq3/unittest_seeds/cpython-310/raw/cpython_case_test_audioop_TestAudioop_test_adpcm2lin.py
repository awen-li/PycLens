# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_adpcm2lin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.adpcm2lin(b'\x07\x7f\x7f', 1, None), (b'\x00\x00\x00\xff\x00\xff', (-179, 40)))
    self.assertEqual(audioop.adpcm2lin(bytearray(b'\x07\x7f\x7f'), 1, None), (b'\x00\x00\x00\xff\x00\xff', (-179, 40)))
    self.assertEqual(audioop.adpcm2lin(memoryview(b'\x07\x7f\x7f'), 1, None), (b'\x00\x00\x00\xff\x00\xff', (-179, 40)))
    self.assertEqual(audioop.adpcm2lin(b'\x07\x7f\x7f', 2, None), (packs[2](0, 11, 41, -22, 114, -179), (-179, 40)))
    self.assertEqual(audioop.adpcm2lin(b'\x07\x7f\x7f', 3, None), (packs[3](0, 2816, 10496, -5632, 29184, -45824), (-179, 40)))
    self.assertEqual(audioop.adpcm2lin(b'\x07\x7f\x7f', 4, None), (packs[4](0, 720896, 2686976, -1441792, 7471104, -11730944), (-179, 40)))
    for w in (1, 2, 3, 4):
        self.assertEqual(audioop.adpcm2lin(b'\x00' * 5, w, None), (b'\x00' * w * 10, (0, 0)))
