# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_uname_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = platform.uname()
    new = res._replace(system='system', node='node', release='release', version='version', machine='machine')
    self.assertEqual(new.system, 'system')
    self.assertEqual(new.node, 'node')
    self.assertEqual(new.release, 'release')
    self.assertEqual(new.version, 'version')
    self.assertEqual(new.machine, 'machine')
    self.assertEqual(new.processor, res.processor)
