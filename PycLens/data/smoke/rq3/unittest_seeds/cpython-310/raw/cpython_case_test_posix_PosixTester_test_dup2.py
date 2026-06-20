# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_dup2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp1 = open(os_helper.TESTFN)
    fp2 = open(os_helper.TESTFN)
    try:
        posix.dup2(fp1.fileno(), fp2.fileno())
    finally:
        fp1.close()
        fp2.close()
