# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m1 = mmap.mmap(-1, 100)
    tagname = 'foo'
    m2 = mmap.mmap(-1, 100, tagname=tagname)
    self.assertEqual(sys.getsizeof(m2), sys.getsizeof(m1) + len(tagname) + 1)
