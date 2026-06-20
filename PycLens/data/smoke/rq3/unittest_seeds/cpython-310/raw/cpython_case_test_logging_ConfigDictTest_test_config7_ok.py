# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_config7_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        self.apply_config(self.config1)
        logger = logging.getLogger('compiler.parser')
        logger.info(self.next_message())
        logger.error(self.next_message())
        self.assert_log_lines([('INFO', '1'), ('ERROR', '2')], stream=output)
        self.assert_log_lines([])
    with support.captured_stdout() as output:
        self.apply_config(self.config7)
        logger = logging.getLogger('compiler.parser')
        self.assertTrue(logger.disabled)
        logger = logging.getLogger('compiler.lexer')
        logger.info(self.next_message())
        logger.error(self.next_message())
        self.assert_log_lines([('INFO', '3'), ('ERROR', '4')], stream=output)
        self.assert_log_lines([])
