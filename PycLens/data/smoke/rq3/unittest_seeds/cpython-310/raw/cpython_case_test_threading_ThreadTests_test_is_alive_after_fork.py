# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_is_alive_after_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_interval = sys.getswitchinterval()
    self.addCleanup(sys.setswitchinterval, old_interval)
    test.support.setswitchinterval(1e-06)
    for i in range(20):
        t = threading.Thread(target=lambda : None)
        t.start()
        pid = os.fork()
        if pid == 0:
            os._exit(11 if t.is_alive() else 10)
        else:
            t.join()
            support.wait_process(pid, exitcode=10)
