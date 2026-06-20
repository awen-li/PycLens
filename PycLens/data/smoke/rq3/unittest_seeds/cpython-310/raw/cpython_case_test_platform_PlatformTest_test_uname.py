# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_uname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = platform.uname()
    self.assertTrue(any(res))
    self.assertEqual(res[0], res.system)
    self.assertEqual(res[-6], res.system)
    self.assertEqual(res[1], res.node)
    self.assertEqual(res[-5], res.node)
    self.assertEqual(res[2], res.release)
    self.assertEqual(res[-4], res.release)
    self.assertEqual(res[3], res.version)
    self.assertEqual(res[-3], res.version)
    self.assertEqual(res[4], res.machine)
    self.assertEqual(res[-2], res.machine)
    self.assertEqual(res[5], res.processor)
    self.assertEqual(res[-1], res.processor)
    self.assertEqual(len(res), 6)
