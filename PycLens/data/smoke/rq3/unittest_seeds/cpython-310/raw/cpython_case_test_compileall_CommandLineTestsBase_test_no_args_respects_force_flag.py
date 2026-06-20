# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_no_args_respects_force_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bazfn = script_helper.make_script(self.directory, 'baz', '')
    with self.temporary_pycache_prefix() as env:
        self.assertRunOK(**env)
        pycpath = importlib.util.cache_from_source(bazfn)
    os.utime(pycpath, (time.time() - 60,) * 2)
    mtime = os.stat(pycpath).st_mtime
    self.assertRunOK(**env)
    mtime2 = os.stat(pycpath).st_mtime
    self.assertEqual(mtime, mtime2)
    self.assertRunOK('-f', **env)
    mtime2 = os.stat(pycpath).st_mtime
    self.assertNotEqual(mtime, mtime2)
