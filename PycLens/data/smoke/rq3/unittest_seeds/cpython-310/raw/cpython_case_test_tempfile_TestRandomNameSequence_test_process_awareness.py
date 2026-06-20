# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestRandomNameSequence_test_process_awareness

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (read_fd, write_fd) = os.pipe()
    pid = None
    try:
        pid = os.fork()
        if not pid:
            os.close(read_fd)
            os.write(write_fd, next(self.r).encode('ascii'))
            os.close(write_fd)
            os._exit(0)
        parent_value = next(self.r)
        child_value = os.read(read_fd, len(parent_value)).decode('ascii')
    finally:
        if pid:
            support.wait_process(pid, exitcode=0)
        os.close(read_fd)
        os.close(write_fd)
    self.assertNotEqual(child_value, parent_value)
