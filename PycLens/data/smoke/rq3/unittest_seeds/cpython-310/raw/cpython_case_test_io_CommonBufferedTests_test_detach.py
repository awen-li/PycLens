# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_detach

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()
    buf = self.tp(raw)
    self.assertIs(buf.detach(), raw)
    self.assertRaises(ValueError, buf.detach)
    repr(buf)
