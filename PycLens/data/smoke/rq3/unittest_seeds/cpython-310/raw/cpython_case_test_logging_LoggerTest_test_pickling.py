# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        for name in ('', 'root', 'foo', 'foo.bar', 'baz.bar'):
            logger = logging.getLogger(name)
            s = pickle.dumps(logger, proto)
            unpickled = pickle.loads(s)
            self.assertIs(unpickled, logger)
