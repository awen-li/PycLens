# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_get_pointer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for flags in (0, ND_PIL):
        nd = ndarray(list(range(3)), shape=[3], flags=flags)
        for i in range(3):
            self.assertEqual(nd[i], get_pointer(nd, [i]))
