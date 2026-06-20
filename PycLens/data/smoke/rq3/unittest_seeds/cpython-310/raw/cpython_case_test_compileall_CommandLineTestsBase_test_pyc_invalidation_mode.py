# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_pyc_invalidation_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    script_helper.make_script(self.pkgdir, 'f1', '')
    pyc = importlib.util.cache_from_source(os.path.join(self.pkgdir, 'f1.py'))
    self.assertRunOK('--invalidation-mode=checked-hash', self.pkgdir)
    with open(pyc, 'rb') as fp:
        data = fp.read()
    self.assertEqual(int.from_bytes(data[4:8], 'little'), 3)
    self.assertRunOK('--invalidation-mode=unchecked-hash', self.pkgdir)
    with open(pyc, 'rb') as fp:
        data = fp.read()
    self.assertEqual(int.from_bytes(data[4:8], 'little'), 1)
