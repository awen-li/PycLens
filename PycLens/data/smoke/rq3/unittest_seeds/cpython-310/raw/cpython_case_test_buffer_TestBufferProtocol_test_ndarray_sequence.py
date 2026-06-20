# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = ndarray(1, shape=())
    self.assertRaises(TypeError, eval, '1 in nd', locals())
    mv = memoryview(nd)
    self.assertEqual(mv, nd)
    self.assertRaises(TypeError, eval, '1 in mv', locals())
    for (fmt, items, _) in iter_format(5):
        nd = ndarray(items, shape=[5], format=fmt)
        for (i, v) in enumerate(nd):
            self.assertEqual(v, items[i])
            self.assertTrue(v in nd)
        if is_memoryview_format(fmt):
            mv = memoryview(nd)
            for (i, v) in enumerate(mv):
                self.assertEqual(v, items[i])
                self.assertTrue(v in mv)
