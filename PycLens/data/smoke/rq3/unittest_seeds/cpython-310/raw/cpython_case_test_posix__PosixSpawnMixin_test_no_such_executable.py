# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_no_such_executable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    no_such_executable = 'no_such_executable'
    try:
        pid = self.spawn_func(no_such_executable, [no_such_executable], os.environ)
    except (FileNotFoundError, PermissionError) as exc:
        self.assertEqual(exc.filename, no_such_executable)
    else:
        (pid2, status) = os.waitpid(pid, 0)
        self.assertEqual(pid2, pid)
        self.assertNotEqual(status, 0)
