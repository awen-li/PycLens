# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestJunkAPIs_test_is_line_junk_REDOS

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    evil_input = '\t' * 1000000 + '##'
    self.assertFalse(difflib.IS_LINE_JUNK(evil_input))
