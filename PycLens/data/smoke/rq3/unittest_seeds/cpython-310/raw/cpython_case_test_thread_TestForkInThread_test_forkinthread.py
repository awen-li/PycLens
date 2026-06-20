# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_thread.py
# case: TestForkInThread_test_forkinthread

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pid = None

    def fork_thread(read_fd, write_fd):
        nonlocal pid
        pid = os.fork()
        if pid:
            return
        try:
            os.close(read_fd)
            os.write(write_fd, b'OK')
        finally:
            os._exit(0)
    with threading_helper.wait_threads_exit():
        thread.start_new_thread(fork_thread, (self.read_fd, self.write_fd))
        self.assertEqual(os.read(self.read_fd, 2), b'OK')
        os.close(self.write_fd)
    self.assertIsNotNone(pid)
    support.wait_process(pid, exitcode=0)
