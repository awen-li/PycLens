# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_io_buffered_by_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen(ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        self.assertIsInstance(p.stdin, io.BufferedIOBase)
        self.assertIsInstance(p.stdout, io.BufferedIOBase)
        self.assertIsInstance(p.stderr, io.BufferedIOBase)
    finally:
        p.stdin.close()
        p.stdout.close()
        p.stderr.close()
        p.wait()
