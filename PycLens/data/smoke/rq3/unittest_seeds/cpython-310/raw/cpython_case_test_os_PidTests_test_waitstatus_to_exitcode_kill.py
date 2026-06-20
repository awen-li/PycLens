# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PidTests_test_waitstatus_to_exitcode_kill

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = f'import time; time.sleep({support.LONG_TIMEOUT})'
    signum = signal.SIGKILL

    def kill_process(pid):
        os.kill(pid, signum)
    self.check_waitpid(code, exitcode=-signum, callback=kill_process)
