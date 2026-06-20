# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_waitid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pid = os.fork()
    if pid == 0:
        os.chdir(os.path.split(sys.executable)[0])
        posix.execve(sys.executable, [sys.executable, '-c', 'pass'], os.environ)
    else:
        res = posix.waitid(posix.P_PID, pid, posix.WEXITED)
        self.assertEqual(pid, res.si_pid)
