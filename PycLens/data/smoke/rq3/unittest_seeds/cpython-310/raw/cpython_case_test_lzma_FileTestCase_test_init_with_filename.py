# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_init_with_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with TempFile(TESTFN, COMPRESSED_XZ):
        with LZMAFile(TESTFN) as f:
            pass
        with LZMAFile(TESTFN, 'w') as f:
            pass
        with LZMAFile(TESTFN, 'a') as f:
            pass
