# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_makedev

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    st = posix.stat(os_helper.TESTFN)
    dev = st.st_dev
    self.assertIsInstance(dev, int)
    self.assertGreaterEqual(dev, 0)
    major = posix.major(dev)
    self.assertIsInstance(major, int)
    self.assertGreaterEqual(major, 0)
    self.assertEqual(posix.major(dev), major)
    self.assertRaises(TypeError, posix.major, float(dev))
    self.assertRaises(TypeError, posix.major)
    self.assertRaises((ValueError, OverflowError), posix.major, -1)
    minor = posix.minor(dev)
    self.assertIsInstance(minor, int)
    self.assertGreaterEqual(minor, 0)
    self.assertEqual(posix.minor(dev), minor)
    self.assertRaises(TypeError, posix.minor, float(dev))
    self.assertRaises(TypeError, posix.minor)
    self.assertRaises((ValueError, OverflowError), posix.minor, -1)
    self.assertEqual(posix.makedev(major, minor), dev)
    self.assertRaises(TypeError, posix.makedev, float(major), minor)
    self.assertRaises(TypeError, posix.makedev, major, float(minor))
    self.assertRaises(TypeError, posix.makedev, major)
    self.assertRaises(TypeError, posix.makedev)
