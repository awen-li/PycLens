# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_cmp_contig

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(cmp_contig(b'123', b'456'))
    x = ndarray(list(range(12)), shape=[3, 4])
    y = ndarray(list(range(12)), shape=[4, 3])
    self.assertFalse(cmp_contig(x, y))
    x = ndarray([1], shape=[1], format='B')
    self.assertTrue(cmp_contig(x, b'\x01'))
    self.assertTrue(cmp_contig(b'\x01', x))
