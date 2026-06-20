# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_setsigmask

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('            import signal\n            signal.raise_signal(signal.SIGUSR1)')
    pid = self.spawn_func(sys.executable, [sys.executable, '-c', code], os.environ, setsigmask=[signal.SIGUSR1])
    support.wait_process(pid, exitcode=0)
