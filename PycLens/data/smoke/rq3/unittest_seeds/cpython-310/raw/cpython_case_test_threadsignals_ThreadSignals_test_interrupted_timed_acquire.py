# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threadsignals.py
# case: ThreadSignals_test_interrupted_timed_acquire

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.start = None
    self.end = None
    self.sigs_recvd = 0
    done = thread.allocate_lock()
    done.acquire()
    lock = thread.allocate_lock()
    lock.acquire()

    def my_handler(signum, frame):
        self.sigs_recvd += 1
    old_handler = signal.signal(signal.SIGUSR1, my_handler)
    try:

        def timed_acquire():
            self.start = time.monotonic()
            lock.acquire(timeout=0.5)
            self.end = time.monotonic()

        def send_signals():
            for _ in range(40):
                time.sleep(0.02)
                os.kill(process_pid, signal.SIGUSR1)
            done.release()
        with threading_helper.wait_threads_exit():
            thread.start_new_thread(send_signals, ())
            timed_acquire()
            done.acquire()
            self.assertLess(self.end - self.start, 2.0)
            self.assertGreater(self.end - self.start, 0.3)
            self.assertGreater(self.sigs_recvd, 0)
    finally:
        signal.signal(signal.SIGUSR1, old_handler)
