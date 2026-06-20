# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_mac_ver_with_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pid = os.fork()
    if pid == 0:
        info = platform.mac_ver()
        os._exit(0)
    else:
        support.wait_process(pid, exitcode=0)
