# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_resetids_explicit_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pid = self.spawn_func(sys.executable, [sys.executable, '-c', 'pass'], os.environ, resetids=False)
    support.wait_process(pid, exitcode=0)
