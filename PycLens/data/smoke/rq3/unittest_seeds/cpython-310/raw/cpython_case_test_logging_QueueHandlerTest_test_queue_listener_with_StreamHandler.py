# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueHandlerTest_test_queue_listener_with_StreamHandler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    listener = logging.handlers.QueueListener(self.queue, self.root_hdlr)
    listener.start()
    try:
        1 / 0
    except ZeroDivisionError as e:
        exc = e
        self.que_logger.exception(self.next_message(), exc_info=exc)
    self.que_logger.error(self.next_message(), stack_info=True)
    listener.stop()
    self.assertEqual(self.stream.getvalue().strip().count('Traceback'), 1)
    self.assertEqual(self.stream.getvalue().strip().count('Stack'), 1)
