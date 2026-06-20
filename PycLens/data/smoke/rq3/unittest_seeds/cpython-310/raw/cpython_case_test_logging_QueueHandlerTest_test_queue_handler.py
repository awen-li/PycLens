# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueHandlerTest_test_queue_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.que_logger.debug(self.next_message())
    self.assertRaises(queue.Empty, self.queue.get_nowait)
    self.que_logger.info(self.next_message())
    self.assertRaises(queue.Empty, self.queue.get_nowait)
    msg = self.next_message()
    self.que_logger.warning(msg)
    data = self.queue.get_nowait()
    self.assertTrue(isinstance(data, logging.LogRecord))
    self.assertEqual(data.name, self.que_logger.name)
    self.assertEqual((data.msg, data.args), (msg, None))
