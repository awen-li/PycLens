# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_config_10_ok

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as output:
        self.apply_config(self.config10)
        logger = logging.getLogger('compiler.parser')
        logger.warning(self.next_message())
        logger = logging.getLogger('compiler')
        logger.warning(self.next_message())
        logger = logging.getLogger('compiler.lexer')
        logger.warning(self.next_message())
        logger = logging.getLogger('compiler.parser.codegen')
        logger.error(self.next_message())
        self.assert_log_lines([('WARNING', '1'), ('ERROR', '4')], stream=output)
