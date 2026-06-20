# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_communicate_epipe_only_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = subprocess.Popen(ZERO_RETURN_CMD, stdin=subprocess.PIPE)
    self.addCleanup(p.stdin.close)
    p.wait()
    p.communicate(b'x' * 2 ** 20)
