# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueHandlerTest_test_queue_listener_with_multiple_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.que_hdlr.setFormatter(self.root_formatter)
    self.que_logger.addHandler(self.root_hdlr)
    listener = logging.handlers.QueueListener(self.queue, self.que_hdlr)
    listener.start()
    self.que_logger.error('error')
    listener.stop()
    self.assertEqual(self.stream.getvalue().strip(), 'que -> ERROR: error')
