# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_force

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRunOK('-q', self.pkgdir)
    pycpath = importlib.util.cache_from_source(self.barfn)
    os.utime(pycpath, (time.time() - 60,) * 2)
    mtime = os.stat(pycpath).st_mtime
    self.assertRunOK('-q', self.pkgdir)
    mtime2 = os.stat(pycpath).st_mtime
    self.assertEqual(mtime, mtime2)
    self.assertRunOK('-q', '-f', self.pkgdir)
    mtime2 = os.stat(pycpath).st_mtime
    self.assertNotEqual(mtime, mtime2)
