# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ConfigDictTest_test_listen_verify

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def verify_fail(stuff):
        return None

    def verify_reverse(stuff):
        return stuff[::-1]
    logger = logging.getLogger('compiler.parser')
    to_send = textwrap.dedent(ConfigFileTest.config1)
    with support.captured_stdout() as output:
        self.setup_via_listener(to_send, verify_fail)
        logger.info(self.next_message())
        logger.error(self.next_message())
    self.assert_log_lines([], stream=output)
    self.assert_log_lines([('INFO', '1'), ('ERROR', '2')], pat='^[\\w.]+ -> (\\w+): (\\d+)$')
    with support.captured_stdout() as output:
        self.setup_via_listener(to_send)
        logger = logging.getLogger('compiler.parser')
        logger.info(self.next_message())
        logger.error(self.next_message())
    self.assert_log_lines([('INFO', '3'), ('ERROR', '4')], stream=output)
    self.assert_log_lines([('INFO', '1'), ('ERROR', '2')], pat='^[\\w.]+ -> (\\w+): (\\d+)$')
    with support.captured_stdout() as output:
        self.setup_via_listener(to_send[::-1], verify_reverse)
        logger = logging.getLogger('compiler.parser')
        logger.info(self.next_message())
        logger.error(self.next_message())
    self.assert_log_lines([('INFO', '5'), ('ERROR', '6')], stream=output)
    self.assert_log_lines([('INFO', '1'), ('ERROR', '2')], pat='^[\\w.]+ -> (\\w+): (\\d+)$')
