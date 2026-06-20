# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_lin2alaw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.lin2alaw(datas[1], 1), b'\xd5\x87\xa4$\xaa*Z')
    self.assertEqual(audioop.lin2alaw(bytearray(datas[1]), 1), b'\xd5\x87\xa4$\xaa*Z')
    self.assertEqual(audioop.lin2alaw(memoryview(datas[1]), 1), b'\xd5\x87\xa4$\xaa*Z')
    for w in (2, 3, 4):
        self.assertEqual(audioop.lin2alaw(datas[w], w), b'\xd5\x87\xa4$\xaa*U')
