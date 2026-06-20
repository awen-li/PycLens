# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_implementation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    levels = {'alpha': 10, 'beta': 11, 'candidate': 12, 'final': 15}
    self.assertTrue(hasattr(sys.implementation, 'name'))
    self.assertTrue(hasattr(sys.implementation, 'version'))
    self.assertTrue(hasattr(sys.implementation, 'hexversion'))
    self.assertTrue(hasattr(sys.implementation, 'cache_tag'))
    version = sys.implementation.version
    self.assertEqual(version[:2], (version.major, version.minor))
    hexversion = version.major << 24 | version.minor << 16 | version.micro << 8 | levels[version.releaselevel] << 4 | version.serial << 0
    self.assertEqual(sys.implementation.hexversion, hexversion)
    self.assertEqual(sys.implementation.name, sys.implementation.name.lower())
