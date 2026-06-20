# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_east_asian_width

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eaw = self.db.east_asian_width
    self.assertRaises(TypeError, eaw, b'a')
    self.assertRaises(TypeError, eaw, bytearray())
    self.assertRaises(TypeError, eaw, '')
    self.assertRaises(TypeError, eaw, 'ra')
    self.assertEqual(eaw('\x1e'), 'N')
    self.assertEqual(eaw(' '), 'Na')
    self.assertEqual(eaw('좔'), 'W')
    self.assertEqual(eaw('ｦ'), 'H')
    self.assertEqual(eaw('？'), 'F')
    self.assertEqual(eaw('‐'), 'A')
    self.assertEqual(eaw('𠀀'), 'W')
