# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_include_bad_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = self.assertRunNotOK('-i', os.path.join(self.directory, 'nosuchfile'), self.pkgdir)
    self.assertRegex(out, b'rror.*nosuchfile')
    self.assertNotRegex(err, b'Traceback')
    self.assertFalse(os.path.exists(importlib.util.cache_from_source(self.pkgdir_cachedir)))
