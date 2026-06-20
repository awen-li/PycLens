# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'abc')
    self.assertIn(ord('a'), b)
    self.assertIn(int(ord('a')), b)
    self.assertNotIn(200, b)
    self.assertRaises(ValueError, lambda : 300 in b)
    self.assertRaises(ValueError, lambda : -1 in b)
    self.assertRaises(ValueError, lambda : sys.maxsize + 1 in b)
    self.assertRaises(TypeError, lambda : None in b)
    self.assertRaises(TypeError, lambda : float(ord('a')) in b)
    self.assertRaises(TypeError, lambda : 'a' in b)
    for f in (bytes, bytearray):
        self.assertIn(f(b''), b)
        self.assertIn(f(b'a'), b)
        self.assertIn(f(b'b'), b)
        self.assertIn(f(b'c'), b)
        self.assertIn(f(b'ab'), b)
        self.assertIn(f(b'bc'), b)
        self.assertIn(f(b'abc'), b)
        self.assertNotIn(f(b'ac'), b)
        self.assertNotIn(f(b'd'), b)
        self.assertNotIn(f(b'dab'), b)
        self.assertNotIn(f(b'abd'), b)
