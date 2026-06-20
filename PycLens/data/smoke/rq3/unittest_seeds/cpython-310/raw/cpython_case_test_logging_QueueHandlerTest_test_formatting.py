# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueHandlerTest_test_formatting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = self.next_message()
    levelname = logging.getLevelName(logging.WARNING)
    log_format_str = '{name} -> {levelname}: {message}'
    formatted_msg = log_format_str.format(name=self.name, levelname=levelname, message=msg)
    formatter = logging.Formatter(self.log_format)
    self.que_hdlr.setFormatter(formatter)
    self.que_logger.warning(msg)
    log_record = self.queue.get_nowait()
    self.assertEqual(formatted_msg, log_record.msg)
    self.assertEqual(formatted_msg, log_record.message)
