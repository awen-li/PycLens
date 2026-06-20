# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_double_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb+') as f:
        f.write(2 ** 16 * b'a')
    with open(TESTFN, 'rb') as f:
        mf = mmap.mmap(f.fileno(), 2 ** 16, access=mmap.ACCESS_READ)
        mf.close()
        mf.close()
