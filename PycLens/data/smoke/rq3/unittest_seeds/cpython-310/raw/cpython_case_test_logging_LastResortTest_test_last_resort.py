# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LastResortTest_test_last_resort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root = self.root_logger
    root.removeHandler(self.root_hdlr)
    old_lastresort = logging.lastResort
    old_raise_exceptions = logging.raiseExceptions
    try:
        with support.captured_stderr() as stderr:
            root.debug('This should not appear')
            self.assertEqual(stderr.getvalue(), '')
            root.warning('Final chance!')
            self.assertEqual(stderr.getvalue(), 'Final chance!\n')
        logging.lastResort = None
        with support.captured_stderr() as stderr:
            root.warning('Final chance!')
            msg = 'No handlers could be found for logger "root"\n'
            self.assertEqual(stderr.getvalue(), msg)
        with support.captured_stderr() as stderr:
            root.warning('Final chance!')
            self.assertEqual(stderr.getvalue(), '')
        root.manager.emittedNoHandlerWarning = False
        logging.raiseExceptions = False
        with support.captured_stderr() as stderr:
            root.warning('Final chance!')
            self.assertEqual(stderr.getvalue(), '')
    finally:
        root.addHandler(self.root_hdlr)
        logging.lastResort = old_lastresort
        logging.raiseExceptions = old_raise_exceptions
