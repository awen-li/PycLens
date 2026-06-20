# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_prot_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mapsize = 10
    with open(TESTFN, 'wb') as fp:
        fp.write(b'a' * mapsize)
    with open(TESTFN, 'rb') as f:
        m = mmap.mmap(f.fileno(), mapsize, prot=mmap.PROT_READ)
        self.assertRaises(TypeError, m.write, 'foo')
