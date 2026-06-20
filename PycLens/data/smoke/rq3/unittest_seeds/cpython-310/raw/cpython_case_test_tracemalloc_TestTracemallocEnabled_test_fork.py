# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestTracemallocEnabled_test_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pid = os.fork()
    if not pid:
        exitcode = 1
        try:
            exitcode = self.fork_child()
        finally:
            os._exit(exitcode)
    else:
        support.wait_process(pid, exitcode=0)
