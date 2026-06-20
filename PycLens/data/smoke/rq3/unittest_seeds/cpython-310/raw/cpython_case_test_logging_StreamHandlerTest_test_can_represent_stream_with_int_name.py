# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: StreamHandlerTest_test_can_represent_stream_with_int_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = logging.StreamHandler(StreamWithIntName())
    self.assertEqual(repr(h), '<StreamHandler 2 (NOTSET)>')
