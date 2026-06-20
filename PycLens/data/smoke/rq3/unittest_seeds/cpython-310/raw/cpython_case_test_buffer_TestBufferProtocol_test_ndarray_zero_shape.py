# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_zero_shape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for flags in (0, ND_PIL):
        nd = ndarray([1, 2, 3], shape=[0], flags=flags)
        mv = memoryview(nd)
        self.assertEqual(mv, nd)
        self.assertEqual(nd.tolist(), [])
        self.assertEqual(mv.tolist(), [])
        nd = ndarray([1, 2, 3], shape=[0, 3, 3], flags=flags)
        self.assertEqual(nd.tolist(), [])
        nd = ndarray([1, 2, 3], shape=[3, 0, 3], flags=flags)
        self.assertEqual(nd.tolist(), [[], [], []])
        nd = ndarray([1, 2, 3], shape=[3, 3, 0], flags=flags)
        self.assertEqual(nd.tolist(), [[[], [], []], [[], [], []], [[], [], []]])
