# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_open_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    outfile = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, outfile)
    script = 'if 1:\n            import sys\n            sys.stdout.write("hello")\n            '
    file_actions = [(os.POSIX_SPAWN_OPEN, 1, outfile, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, stat.S_IRUSR | stat.S_IWUSR)]
    args = self.python_args('-c', script)
    pid = self.spawn_func(args[0], args, os.environ, file_actions=file_actions)
    support.wait_process(pid, exitcode=0)
    with open(outfile, encoding='utf-8') as f:
        self.assertEqual(f.read(), 'hello')
