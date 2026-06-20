# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_sizeof
    vsize = support.calcvobjsize
    base_struct = 'Pnin 2P2n2i5P P'
    per_dim = '3n'
    items = list(range(8))
    check(memoryview(b''), vsize(base_struct + 1 * per_dim))
    a = ndarray(items, shape=[2, 4], format='b')
    check(memoryview(a), vsize(base_struct + 2 * per_dim))
    a = ndarray(items, shape=[2, 2, 2], format='b')
    check(memoryview(a), vsize(base_struct + 3 * per_dim))
