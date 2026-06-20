# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_getwindowsversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test.support.get_attribute(sys, 'getwindowsversion')
    v = sys.getwindowsversion()
    self.assertEqual(len(v), 5)
    self.assertIsInstance(v[0], int)
    self.assertIsInstance(v[1], int)
    self.assertIsInstance(v[2], int)
    self.assertIsInstance(v[3], int)
    self.assertIsInstance(v[4], str)
    self.assertRaises(IndexError, operator.getitem, v, 5)
    self.assertIsInstance(v.major, int)
    self.assertIsInstance(v.minor, int)
    self.assertIsInstance(v.build, int)
    self.assertIsInstance(v.platform, int)
    self.assertIsInstance(v.service_pack, str)
    self.assertIsInstance(v.service_pack_minor, int)
    self.assertIsInstance(v.service_pack_major, int)
    self.assertIsInstance(v.suite_mask, int)
    self.assertIsInstance(v.product_type, int)
    self.assertEqual(v[0], v.major)
    self.assertEqual(v[1], v.minor)
    self.assertEqual(v[2], v.build)
    self.assertEqual(v[3], v.platform)
    self.assertEqual(v[4], v.service_pack)
    (maj, min, buildno, plat, csd) = sys.getwindowsversion()
