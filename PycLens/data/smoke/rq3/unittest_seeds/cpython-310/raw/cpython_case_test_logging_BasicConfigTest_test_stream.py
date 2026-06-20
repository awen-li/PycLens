# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_stream

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stream = io.StringIO()
    self.addCleanup(stream.close)
    logging.basicConfig(stream=stream)
    self.assertEqual(len(logging.root.handlers), 1)
    handler = logging.root.handlers[0]
    self.assertIsInstance(handler, logging.StreamHandler)
    self.assertEqual(handler.stream, stream)
