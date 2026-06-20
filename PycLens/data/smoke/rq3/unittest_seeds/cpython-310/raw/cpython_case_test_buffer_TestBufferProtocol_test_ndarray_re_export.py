# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_re_export

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nd = ndarray(items, shape=[3, 4], flags=ND_PIL)
    ex = ndarray(nd)
    self.assertTrue(ex.flags & ND_PIL)
    self.assertIs(ex.obj, nd)
    self.assertEqual(ex.suboffsets, (0, -1))
    self.assertFalse(ex.c_contiguous)
    self.assertFalse(ex.f_contiguous)
    self.assertFalse(ex.contiguous)
