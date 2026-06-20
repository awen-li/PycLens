# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_close_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    closefile = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, closefile)
    script = f"if 1:\n            import os\n            try:\n                os.fstat(0)\n            except OSError as e:\n                with open({closefile!r}, 'w', encoding='utf-8') as closefile:\n                    closefile.write('is closed %d' % e.errno)\n            "
    args = self.python_args('-c', script)
    pid = self.spawn_func(args[0], args, os.environ, file_actions=[(os.POSIX_SPAWN_CLOSE, 0)])
    support.wait_process(pid, exitcode=0)
    with open(closefile, encoding='utf-8') as f:
        self.assertEqual(f.read(), 'is closed %d' % errno.EBADF)
