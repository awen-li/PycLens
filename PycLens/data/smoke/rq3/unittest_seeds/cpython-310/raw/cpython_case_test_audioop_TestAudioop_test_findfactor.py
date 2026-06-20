# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_findfactor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.findfactor(datas[2], datas[2]), 1.0)
    self.assertEqual(audioop.findfactor(bytearray(datas[2]), bytearray(datas[2])), 1.0)
    self.assertEqual(audioop.findfactor(memoryview(datas[2]), memoryview(datas[2])), 1.0)
    self.assertEqual(audioop.findfactor(b'\x00' * len(datas[2]), datas[2]), 0.0)
