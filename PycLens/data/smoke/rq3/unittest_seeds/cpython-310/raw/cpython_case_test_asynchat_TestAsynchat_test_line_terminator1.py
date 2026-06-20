# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestAsynchat_test_line_terminator1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for l in (1, 2, 3):
        self.line_terminator_check(b'\n', l)
