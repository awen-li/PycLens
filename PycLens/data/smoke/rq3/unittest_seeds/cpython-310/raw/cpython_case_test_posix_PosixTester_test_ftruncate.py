# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_ftruncate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = open(os_helper.TESTFN, 'w+')
    try:
        fp.write('test')
        fp.flush()
        posix.ftruncate(fp.fileno(), 0)
    finally:
        fp.close()
