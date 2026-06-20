# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_findfit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.findfit(datas[2], datas[2]), (0, 1.0))
    self.assertEqual(audioop.findfit(bytearray(datas[2]), bytearray(datas[2])), (0, 1.0))
    self.assertEqual(audioop.findfit(memoryview(datas[2]), memoryview(datas[2])), (0, 1.0))
    self.assertEqual(audioop.findfit(datas[2], packs[2](1, 2, 0)), (1, 8038.8))
    self.assertEqual(audioop.findfit(datas[2][:-2] * 5 + datas[2], datas[2]), (30, 1.0))
