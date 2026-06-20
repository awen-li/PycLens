# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueListenerTest_test_no_messages_in_queue_after_stop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.skip_if_broken_multiprocessing_synchronize()
    for i in range(self.repeat):
        queue = multiprocessing.Queue()
        self.setup_and_log(queue, '%s_%s' % (self.id(), i))
        items = list(self.get_all_from_queue(queue))
        queue.close()
        queue.join_thread()
        expected = [[], [logging.handlers.QueueListener._sentinel]]
        self.assertIn(items, expected, 'Found unexpected messages in queue: %s' % [m.msg if isinstance(m, logging.LogRecord) else m for m in items])
