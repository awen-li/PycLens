# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TempFile(TESTFN):
        with LZMAFile(TESTFN, 'r'):
            pass
        with LZMAFile(TESTFN, 'rb'):
            pass
        with LZMAFile(TESTFN, 'w'):
            pass
        with LZMAFile(TESTFN, 'wb'):
            pass
        with LZMAFile(TESTFN, 'a'):
            pass
        with LZMAFile(TESTFN, 'ab'):
            pass
