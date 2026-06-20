# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_index_setitem_single

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (fmt, items, single_item) in iter_format(5):
        nd = ndarray(items, shape=[5], format=fmt, flags=ND_WRITABLE)
        for i in range(5):
            items[i] = single_item
            nd[i] = single_item
        self.assertEqual(nd.tolist(), items)
        self.assertRaises(IndexError, nd.__setitem__, -6, single_item)
        self.assertRaises(IndexError, nd.__setitem__, 5, single_item)
        if not is_memoryview_format(fmt):
            continue
        nd = ndarray(items, shape=[5], format=fmt, flags=ND_WRITABLE)
        mv = memoryview(nd)
        self.assertEqual(mv, nd)
        for i in range(5):
            items[i] = single_item
            mv[i] = single_item
        self.assertEqual(mv.tolist(), items)
        self.assertRaises(IndexError, mv.__setitem__, -6, single_item)
        self.assertRaises(IndexError, mv.__setitem__, 5, single_item)
    for (fmt, items, single_item) in iter_format(5):
        nd = ndarray(items, shape=[5], format=fmt, flags=ND_WRITABLE)
        for i in range(-5, 4):
            items[i] = items[i + 1]
            nd[i] = nd[i + 1]
        self.assertEqual(nd.tolist(), items)
        if not is_memoryview_format(fmt):
            continue
        nd = ndarray(items, shape=[5], format=fmt, flags=ND_WRITABLE)
        mv = memoryview(nd)
        self.assertEqual(mv, nd)
        for i in range(-5, 4):
            items[i] = items[i + 1]
            mv[i] = mv[i + 1]
        self.assertEqual(mv.tolist(), items)
