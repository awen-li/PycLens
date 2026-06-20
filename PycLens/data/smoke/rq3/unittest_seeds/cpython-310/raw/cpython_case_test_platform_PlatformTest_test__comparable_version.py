# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test__comparable_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from platform import _comparable_version as V
    self.assertEqual(V('1.2.3'), V('1.2.3'))
    self.assertLess(V('1.2.3'), V('1.2.10'))
    self.assertEqual(V('1.2.3.4'), V('1_2-3+4'))
    self.assertLess(V('1.2spam'), V('1.2dev'))
    self.assertLess(V('1.2dev'), V('1.2alpha'))
    self.assertLess(V('1.2dev'), V('1.2a'))
    self.assertLess(V('1.2alpha'), V('1.2beta'))
    self.assertLess(V('1.2a'), V('1.2b'))
    self.assertLess(V('1.2beta'), V('1.2c'))
    self.assertLess(V('1.2b'), V('1.2c'))
    self.assertLess(V('1.2c'), V('1.2RC'))
    self.assertLess(V('1.2c'), V('1.2rc'))
    self.assertLess(V('1.2RC'), V('1.2.0'))
    self.assertLess(V('1.2rc'), V('1.2.0'))
    self.assertLess(V('1.2.0'), V('1.2pl'))
    self.assertLess(V('1.2.0'), V('1.2p'))
    self.assertLess(V('1.5.1'), V('1.5.2b2'))
    self.assertLess(V('3.10a'), V('161'))
    self.assertEqual(V('8.02'), V('8.02'))
    self.assertLess(V('3.4j'), V('1996.07.12'))
    self.assertLess(V('3.1.1.6'), V('3.2.pl0'))
    self.assertLess(V('2g6'), V('11g'))
    self.assertLess(V('0.9'), V('2.2'))
    self.assertLess(V('1.2'), V('1.2.1'))
    self.assertLess(V('1.1'), V('1.2.2'))
    self.assertLess(V('1.1'), V('1.2'))
    self.assertLess(V('1.2.1'), V('1.2.2'))
    self.assertLess(V('1.2'), V('1.2.2'))
    self.assertLess(V('0.4'), V('0.4.0'))
    self.assertLess(V('1.13++'), V('5.5.kw'))
    self.assertLess(V('0.960923'), V('2.2beta29'))
