# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueListenerTest_test_calls_task_done_after_stop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    log_queue = queue.Queue()
    listener = logging.handlers.QueueListener(log_queue)
    listener.start()
    listener.stop()
    with self.assertRaises(ValueError):
        log_queue.task_done()
