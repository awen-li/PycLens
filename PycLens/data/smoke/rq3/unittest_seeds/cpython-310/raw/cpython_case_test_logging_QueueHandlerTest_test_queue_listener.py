# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueHandlerTest_test_queue_listener

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = TestHandler(support.Matcher())
    listener = logging.handlers.QueueListener(self.queue, handler)
    listener.start()
    try:
        self.que_logger.warning(self.next_message())
        self.que_logger.error(self.next_message())
        self.que_logger.critical(self.next_message())
    finally:
        listener.stop()
    self.assertTrue(handler.matches(levelno=logging.WARNING, message='1'))
    self.assertTrue(handler.matches(levelno=logging.ERROR, message='2'))
    self.assertTrue(handler.matches(levelno=logging.CRITICAL, message='3'))
    handler.close()
    handler = TestHandler(support.Matcher())
    handler.setLevel(logging.CRITICAL)
    listener = logging.handlers.QueueListener(self.queue, handler, respect_handler_level=True)
    listener.start()
    try:
        self.que_logger.warning(self.next_message())
        self.que_logger.error(self.next_message())
        self.que_logger.critical(self.next_message())
    finally:
        listener.stop()
    self.assertFalse(handler.matches(levelno=logging.WARNING, message='4'))
    self.assertFalse(handler.matches(levelno=logging.ERROR, message='5'))
    self.assertTrue(handler.matches(levelno=logging.CRITICAL, message='6'))
    handler.close()
