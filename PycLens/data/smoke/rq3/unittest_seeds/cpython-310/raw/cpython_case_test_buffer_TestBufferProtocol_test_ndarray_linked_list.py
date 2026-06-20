# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_linked_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for perm in permutations(range(5)):
        m = [0] * 5
        nd = ndarray([1, 2, 3], shape=[3], flags=ND_VAREXPORT)
        m[0] = memoryview(nd)
        for i in range(1, 5):
            nd.push([1, 2, 3], shape=[3])
            m[i] = memoryview(nd)
        for i in range(5):
            m[perm[i]].release()
        self.assertRaises(BufferError, nd.pop)
        del nd
