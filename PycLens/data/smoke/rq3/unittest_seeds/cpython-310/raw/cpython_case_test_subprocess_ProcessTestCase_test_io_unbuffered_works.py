# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_io_unbuffered_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen(ZERO_RETURN_CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)
    try:
        self.assertIsInstance(p.stdin, io.RawIOBase)
        self.assertIsInstance(p.stdout, io.RawIOBase)
        self.assertIsInstance(p.stderr, io.RawIOBase)
    finally:
        p.stdin.close()
        p.stdout.close()
        p.stderr.close()
        p.wait()
