# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_empty_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open(TESTFN, 'w+b')
    f.close()
    with open(TESTFN, 'rb') as f:
        self.assertRaisesRegex(ValueError, 'cannot mmap an empty file', mmap.mmap, f.fileno(), 0, access=mmap.ACCESS_READ)
