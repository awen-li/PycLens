# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: WarningsTest_test_warnings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        logging.captureWarnings(True)
        self.addCleanup(logging.captureWarnings, False)
        warnings.filterwarnings('always', category=UserWarning)
        stream = io.StringIO()
        h = logging.StreamHandler(stream)
        logger = logging.getLogger('py.warnings')
        logger.addHandler(h)
        warnings.warn("I'm warning you...")
        logger.removeHandler(h)
        s = stream.getvalue()
        h.close()
        self.assertGreater(s.find("UserWarning: I'm warning you...\n"), 0)
        a_file = io.StringIO()
        warnings.showwarning('Explicit', UserWarning, 'dummy.py', 42, a_file, 'Dummy line')
        s = a_file.getvalue()
        a_file.close()
        self.assertEqual(s, 'dummy.py:42: UserWarning: Explicit\n  Dummy line\n')
