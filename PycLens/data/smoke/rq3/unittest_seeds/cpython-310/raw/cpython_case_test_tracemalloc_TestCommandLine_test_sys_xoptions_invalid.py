# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestCommandLine_test_sys_xoptions_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for nframe in INVALID_NFRAME:
        with self.subTest(nframe=nframe):
            self.check_sys_xoptions_invalid(nframe)
