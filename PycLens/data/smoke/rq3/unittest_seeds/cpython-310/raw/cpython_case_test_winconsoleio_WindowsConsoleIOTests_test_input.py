# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertStdinRoundTrip('abc123')
    self.assertStdinRoundTrip('ϼўТλФЙ')
    self.assertStdinRoundTrip('A͏B ﬖ̳AA̝')
