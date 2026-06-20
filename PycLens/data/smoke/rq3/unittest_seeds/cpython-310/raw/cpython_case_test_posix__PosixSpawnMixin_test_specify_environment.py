# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: _PosixSpawnMixin_test_specify_environment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    envfile = os_helper.TESTFN
    self.addCleanup(os_helper.unlink, envfile)
    script = f"""if 1:\n            import os\n            with open({envfile!r}, "w", encoding="utf-8") as envfile:\n                envfile.write(os.environ['foo'])\n        """
    args = self.python_args('-c', script)
    pid = self.spawn_func(args[0], args, {**os.environ, 'foo': 'bar'})
    support.wait_process(pid, exitcode=0)
    with open(envfile, encoding='utf-8') as f:
        self.assertEqual(f.read(), 'bar')
