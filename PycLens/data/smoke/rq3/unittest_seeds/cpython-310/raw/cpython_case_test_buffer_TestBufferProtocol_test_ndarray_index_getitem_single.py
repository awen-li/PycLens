# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_index_getitem_single

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (fmt, items, _) in iter_format(5):
        nd = ndarray(items, shape=[5], format=fmt)
        for i in range(-5, 5):
            self.assertEqual(nd[i], items[i])
        self.assertRaises(IndexError, nd.__getitem__, -6)
        self.assertRaises(IndexError, nd.__getitem__, 5)
        if is_memoryview_format(fmt):
            mv = memoryview(nd)
            self.assertEqual(mv, nd)
            for i in range(-5, 5):
                self.assertEqual(mv[i], items[i])
            self.assertRaises(IndexError, mv.__getitem__, -6)
            self.assertRaises(IndexError, mv.__getitem__, 5)
    for (fmt, items, _) in iter_format(5):
        ex = ndarray(items, shape=[5], flags=ND_WRITABLE, format=fmt)
        nd = ndarray(ex, getbuf=PyBUF_CONTIG | PyBUF_FORMAT)
        for i in range(-5, 5):
            self.assertEqual(nd[i], items[i])
        if is_memoryview_format(fmt):
            mv = nd.memoryview_from_buffer()
            self.assertIs(mv.__eq__(nd), NotImplemented)
            for i in range(-5, 5):
                self.assertEqual(mv[i], items[i])
    items = [1, 2, 3, 4, 5]
    ex = ndarray(items, shape=[5])
    nd = ndarray(ex, getbuf=PyBUF_CONTIG_RO)
    for i in range(-5, 5):
        self.assertEqual(nd[i], items[i])
    items = [1, 2, 3, 4, 5]
    ex = ndarray(items, shape=[5])
    nd = ndarray(ex, getbuf=PyBUF_SIMPLE)
    for i in range(-5, 5):
        self.assertEqual(nd[i], items[i])
