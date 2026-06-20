# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_double_close_on_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fds = []

    def open_fds():
        for i in range(20):
            fds.extend(os.pipe())
            time.sleep(0.001)
    t = threading.Thread(target=open_fds)
    t.start()
    try:
        with self.assertRaises(EnvironmentError):
            subprocess.Popen(NONEXISTING_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    finally:
        t.join()
        exc = None
        for fd in fds:
            try:
                os.close(fd)
            except OSError as e:
                exc = e
        if exc is not None:
            raise exc
