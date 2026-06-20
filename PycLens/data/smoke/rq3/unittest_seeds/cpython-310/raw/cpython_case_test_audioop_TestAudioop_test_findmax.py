# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_findmax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.findmax(datas[2], 1), 5)
    self.assertEqual(audioop.findmax(bytearray(datas[2]), 1), 5)
    self.assertEqual(audioop.findmax(memoryview(datas[2]), 1), 5)
