# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_returns_pid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pidfile = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, pidfile)
    script = f'if 1:\n            import os\n            with open({pidfile!r}, "w") as pidfile:\n                pidfile.write(str(os.getpid()))\n            '
    args = self.python_args('-c', script)
    pid = self.spawn_func(args[0], args, os.environ)
    support.wait_process(pid, exitcode=0)
    with open(pidfile, encoding='utf-8') as f:
        self.assertEqual(f.read(), str(pid))
