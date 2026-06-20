# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_setsigdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_handler = signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    code = textwrap.dedent('            import signal\n            signal.raise_signal(signal.SIGUSR1)')
    try:
        pid = self.spawn_func(sys.executable, [sys.executable, '-c', code], os.environ, setsigdef=[signal.SIGUSR1])
    finally:
        signal.signal(signal.SIGUSR1, original_handler)
    support.wait_process(pid, exitcode=-signal.SIGUSR1)
