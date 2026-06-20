# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: MemoryHandlerTest_test_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.mem_logger.debug(self.next_message())
    self.assert_log_lines([])
    self.mem_logger.info(self.next_message())
    self.assert_log_lines([])
    self.mem_logger.warning(self.next_message())
    lines = [('DEBUG', '1'), ('INFO', '2'), ('WARNING', '3')]
    self.assert_log_lines(lines)
    for n in (4, 14):
        for i in range(9):
            self.mem_logger.debug(self.next_message())
        self.assert_log_lines(lines)
        self.mem_logger.debug(self.next_message())
        lines = lines + [('DEBUG', str(i)) for i in range(n, n + 10)]
        self.assert_log_lines(lines)
    self.mem_logger.debug(self.next_message())
    self.assert_log_lines(lines)
