# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: HandlerTest_test_post_fork_child_no_deadlock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class _OurHandler(logging.Handler):

        def __init__(self):
            super().__init__()
            self.sub_handler = logging.StreamHandler(stream=open('/dev/null', 'wt', encoding='utf-8'))

        def emit(self, record):
            self.sub_handler.acquire()
            try:
                self.sub_handler.emit(record)
            finally:
                self.sub_handler.release()
    self.assertEqual(len(logging._handlers), 0)
    refed_h = _OurHandler()
    self.addCleanup(refed_h.sub_handler.stream.close)
    refed_h.name = 'because we need at least one for this test'
    self.assertGreater(len(logging._handlers), 0)
    self.assertGreater(len(logging._at_fork_reinit_lock_weakset), 1)
    test_logger = logging.getLogger('test_post_fork_child_no_deadlock')
    test_logger.addHandler(refed_h)
    test_logger.setLevel(logging.DEBUG)
    locks_held__ready_to_fork = threading.Event()
    fork_happened__release_locks_and_end_thread = threading.Event()

    def lock_holder_thread_fn():
        logging._acquireLock()
        try:
            refed_h.acquire()
            try:
                locks_held__ready_to_fork.set()
                fork_happened__release_locks_and_end_thread.wait(0.5)
            finally:
                refed_h.release()
        finally:
            logging._releaseLock()
    lock_holder_thread = threading.Thread(target=lock_holder_thread_fn, name='test_post_fork_child_no_deadlock lock holder')
    lock_holder_thread.start()
    locks_held__ready_to_fork.wait()
    pid = os.fork()
    if pid == 0:
        try:
            test_logger.info('Child process did not deadlock. \\o/')
        finally:
            os._exit(0)
    else:
        test_logger.info('Parent process returned from fork. \\o/')
        fork_happened__release_locks_and_end_thread.set()
        lock_holder_thread.join()
        support.wait_process(pid, exitcode=0)
