# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_tagname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data1 = b'0123456789'
    data2 = b'abcdefghij'
    assert len(data1) == len(data2)
    m1 = mmap.mmap(-1, len(data1), tagname='foo')
    m1[:] = data1
    m2 = mmap.mmap(-1, len(data2), tagname='foo')
    m2[:] = data2
    self.assertEqual(m1[:], data2)
    self.assertEqual(m2[:], data2)
    m2.close()
    m1.close()
    m1 = mmap.mmap(-1, len(data1), tagname='foo')
    m1[:] = data1
    m2 = mmap.mmap(-1, len(data2), tagname='boo')
    m2[:] = data2
    self.assertEqual(m1[:], data1)
    self.assertEqual(m2[:], data2)
    m2.close()
    m1.close()
