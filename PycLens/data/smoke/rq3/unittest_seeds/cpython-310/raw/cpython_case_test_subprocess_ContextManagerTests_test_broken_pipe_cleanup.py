# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ContextManagerTests_test_broken_pipe_cleanup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proc = subprocess.Popen(ZERO_RETURN_CMD, stdin=subprocess.PIPE, bufsize=support.PIPE_MAX_SIZE * 2)
    proc = proc.__enter__()
    proc.stdin.write(b'x' * support.PIPE_MAX_SIZE)
    self.assertIsNone(proc.returncode)
    self.assertRaises(OSError, proc.__exit__, None, None, None)
    self.assertEqual(proc.returncode, 0)
    self.assertTrue(proc.stdin.closed)
