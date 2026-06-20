# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_no_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logging.basicConfig()
    self.assertEqual(len(logging.root.handlers), 1)
    handler = logging.root.handlers[0]
    self.assertIsInstance(handler, logging.StreamHandler)
    self.assertEqual(handler.stream, sys.stderr)
    formatter = handler.formatter
    self.assertEqual(formatter._style._fmt, logging.BASIC_FORMAT)
    self.assertIsNone(formatter.datefmt)
    self.assertIsInstance(formatter._style, logging.PercentStyle)
    self.assertEqual(logging.root.level, self.original_logging_level)
