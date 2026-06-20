# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: StreamHandlerTest_test_stream_setting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = logging.StreamHandler()
    stream = io.StringIO()
    old = h.setStream(stream)
    self.assertIs(old, sys.stderr)
    actual = h.setStream(old)
    self.assertIs(actual, stream)
    actual = h.setStream(old)
    self.assertIsNone(actual)
