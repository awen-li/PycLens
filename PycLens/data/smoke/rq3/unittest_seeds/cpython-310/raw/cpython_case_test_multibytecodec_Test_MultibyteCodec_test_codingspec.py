# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_MultibyteCodec_test_codingspec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        for enc in ALL_CJKENCODINGS:
            code = '# coding: {}\n'.format(enc)
            exec(code)
    finally:
        os_helper.unlink(TESTFN)
