# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_dup2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dupfile = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, dupfile)
    script = 'if 1:\n            import sys\n            sys.stdout.write("hello")\n            '
    with open(dupfile, 'wb') as childfile:
        file_actions = [(os.POSIX_SPAWN_DUP2, childfile.fileno(), 1)]
        args = self.python_args('-c', script)
        pid = self.spawn_func(args[0], args, os.environ, file_actions=file_actions)
        support.wait_process(pid, exitcode=0)
    with open(dupfile, encoding='utf-8') as f:
        self.assertEqual(f.read(), 'hello')
