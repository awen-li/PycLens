# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_poll_blocks_with_negative_ms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for timeout_ms in [None, -1000, -1, -1.0, -0.1, -1e-100]:
        (r, w) = os.pipe()
        pollster = select.poll()
        pollster.register(r, select.POLLIN)
        poll_thread = threading.Thread(target=pollster.poll, args=(timeout_ms,))
        poll_thread.start()
        poll_thread.join(timeout=0.1)
        self.assertTrue(poll_thread.is_alive())
        os.write(w, b'spam')
        poll_thread.join()
        self.assertFalse(poll_thread.is_alive())
        os.close(r)
        os.close(w)
