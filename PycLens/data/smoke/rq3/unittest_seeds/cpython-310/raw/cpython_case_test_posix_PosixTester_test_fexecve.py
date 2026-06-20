# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_fexecve

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = os.open(sys.executable, os.O_RDONLY)
    try:
        pid = os.fork()
        if pid == 0:
            os.chdir(os.path.split(sys.executable)[0])
            posix.execve(fp, [sys.executable, '-c', 'pass'], os.environ)
        else:
            support.wait_process(pid, exitcode=0)
    finally:
        os.close(fp)
