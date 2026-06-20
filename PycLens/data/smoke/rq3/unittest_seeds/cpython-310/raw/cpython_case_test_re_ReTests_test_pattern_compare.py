# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_pattern_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern1 = re.compile('abc', re.IGNORECASE)
    self.assertEqual(pattern1, pattern1)
    self.assertFalse(pattern1 != pattern1)
    re.purge()
    pattern2 = re.compile('abc', re.IGNORECASE)
    self.assertEqual(hash(pattern2), hash(pattern1))
    self.assertEqual(pattern2, pattern1)
    re.purge()
    pattern3 = re.compile('XYZ', re.IGNORECASE)
    self.assertNotEqual(pattern3, pattern1)
    re.purge()
    pattern4 = re.compile('abc')
    self.assertNotEqual(pattern4, pattern1)
    with self.assertRaises(TypeError):
        pattern1 < pattern2
