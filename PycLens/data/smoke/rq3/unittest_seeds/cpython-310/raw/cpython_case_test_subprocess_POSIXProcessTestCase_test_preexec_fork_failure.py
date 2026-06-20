# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: POSIXProcessTestCase_test_preexec_fork_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        from resource import getrlimit, setrlimit, RLIMIT_NPROC
    except ImportError as err:
        self.skipTest(err)
    limits = getrlimit(RLIMIT_NPROC)
    [_, hard] = limits
    setrlimit(RLIMIT_NPROC, (0, hard))
    self.addCleanup(setrlimit, RLIMIT_NPROC, limits)
    try:
        subprocess.call([sys.executable, '-c', ''], preexec_fn=lambda : None)
    except BlockingIOError:
        pass
    else:
        self.skipTest('RLIMIT_NPROC had no effect; probably superuser')
