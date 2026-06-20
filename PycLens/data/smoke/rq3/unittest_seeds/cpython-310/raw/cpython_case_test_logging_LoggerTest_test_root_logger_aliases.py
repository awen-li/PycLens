# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_root_logger_aliases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = logging.getLogger()
    self.assertIs(root, logging.root)
    self.assertIs(root, logging.getLogger(None))
    self.assertIs(root, logging.getLogger(''))
    self.assertIs(root, logging.getLogger('root'))
    self.assertIs(root, logging.getLogger('foo').root)
    self.assertIs(root, logging.getLogger('foo.bar').root)
    self.assertIs(root, logging.getLogger('foo').parent)
    self.assertIsNot(root, logging.getLogger('\x00'))
    self.assertIsNot(root, logging.getLogger('foo.bar').parent)
