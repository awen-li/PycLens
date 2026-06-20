# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: QueueListenerTest_test_handle_called_with_mp_queue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.skip_if_broken_multiprocessing_synchronize()
    for i in range(self.repeat):
        log_queue = multiprocessing.Queue()
        self.setup_and_log(log_queue, '%s_%s' % (self.id(), i))
        log_queue.close()
        log_queue.join_thread()
    self.assertEqual(mock_handle.call_count, 5 * self.repeat, 'correct number of handled log messages')
