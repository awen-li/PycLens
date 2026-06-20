# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: MemoryTest_test_persistent_loggers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.root_logger.setLevel(logging.INFO)
    foo = logging.getLogger('foo')
    self._watch_for_survival(foo)
    foo.setLevel(logging.DEBUG)
    self.root_logger.debug(self.next_message())
    foo.debug(self.next_message())
    self.assert_log_lines([('foo', 'DEBUG', '2')])
    del foo
    self._assertTruesurvival()
    bar = logging.getLogger('foo')
    bar.debug(self.next_message())
    self.assert_log_lines([('foo', 'DEBUG', '2'), ('foo', 'DEBUG', '3')])
