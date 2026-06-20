# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: WarningsTest_test_warnings_no_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        logging.captureWarnings(True)
        self.addCleanup(logging.captureWarnings, False)
        logger = logging.getLogger('py.warnings')
        self.assertEqual(logger.handlers, [])
        warnings.showwarning('Explicit', UserWarning, 'dummy.py', 42)
        self.assertEqual(len(logger.handlers), 1)
        self.assertIsInstance(logger.handlers[0], logging.NullHandler)
