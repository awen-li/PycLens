# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: MemoryHandlerTest_test_flush_on_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.mem_logger.debug(self.next_message())
    self.assert_log_lines([])
    self.mem_logger.info(self.next_message())
    self.assert_log_lines([])
    self.mem_logger.removeHandler(self.mem_hdlr)
    self.mem_hdlr.close()
    lines = [('DEBUG', '1'), ('INFO', '2')]
    self.assert_log_lines(lines)
    self.mem_hdlr = logging.handlers.MemoryHandler(10, logging.WARNING, self.root_hdlr, False)
    self.mem_logger.addHandler(self.mem_hdlr)
    self.mem_logger.debug(self.next_message())
    self.assert_log_lines(lines)
    self.mem_logger.info(self.next_message())
    self.assert_log_lines(lines)
    self.mem_logger.removeHandler(self.mem_hdlr)
    self.mem_hdlr.close()
    self.assert_log_lines(lines)
