# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_random_formats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 10
    for char in fmtdict['@m']:
        (fmt, items, singleitem) = randitems(n, 'memoryview', '@', char)
        for flags in (0, ND_PIL):
            nd = ndarray(items, shape=[n], format=fmt, flags=flags)
            m = memoryview(nd)
            self.assertEqual(m, nd)
            nd = nd[::-3]
            m = memoryview(nd)
            self.assertEqual(m, nd)
    n = 10
    for _ in range(100):
        (fmt, items, singleitem) = randitems(n)
        for flags in (0, ND_PIL):
            nd = ndarray(items, shape=[n], format=fmt, flags=flags)
            m = memoryview(nd)
            self.assertEqual(m, nd)
            nd = nd[::-3]
            m = memoryview(nd)
            self.assertEqual(m, nd)
