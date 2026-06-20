# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poll.py
# case: PollTests_test_threaded_poll

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, w) = os.pipe()
    self.addCleanup(os.close, r)
    self.addCleanup(os.close, w)
    rfds = []
    for i in range(10):
        fd = os.dup(r)
        self.addCleanup(os.close, fd)
        rfds.append(fd)
    pollster = select.poll()
    for fd in rfds:
        pollster.register(fd, select.POLLIN)
    t = threading.Thread(target=pollster.poll)
    t.start()
    try:
        time.sleep(0.5)
        for fd in rfds:
            pollster.unregister(fd)
        pollster.register(w, select.POLLOUT)
        self.assertRaises(RuntimeError, pollster.poll)
    finally:
        os.write(w, b'spam')
        t.join()
