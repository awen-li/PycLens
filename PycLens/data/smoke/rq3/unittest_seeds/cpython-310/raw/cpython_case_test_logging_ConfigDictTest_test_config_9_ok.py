# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_config_9_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        self.apply_config(self.config9)
        logger = logging.getLogger('compiler.parser')
        logger.info(self.next_message())
        self.assert_log_lines([], stream=output)
        self.apply_config(self.config9a)
        logger.info(self.next_message())
        self.assert_log_lines([], stream=output)
        self.apply_config(self.config9b)
        logger.info(self.next_message())
        self.assert_log_lines([('INFO', '3')], stream=output)
