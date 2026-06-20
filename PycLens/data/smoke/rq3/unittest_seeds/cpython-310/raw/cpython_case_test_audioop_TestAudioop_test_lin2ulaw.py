# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audioop.py
# case: TestAudioop_test_lin2ulaw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(audioop.lin2ulaw(datas[1], 1), b'\xff\xad\x8e\x0e\x80\x00g')
    self.assertEqual(audioop.lin2ulaw(bytearray(datas[1]), 1), b'\xff\xad\x8e\x0e\x80\x00g')
    self.assertEqual(audioop.lin2ulaw(memoryview(datas[1]), 1), b'\xff\xad\x8e\x0e\x80\x00g')
    for w in (2, 3, 4):
        self.assertEqual(audioop.lin2ulaw(datas[w], w), b'\xff\xad\x8e\x0e\x80\x00~')
