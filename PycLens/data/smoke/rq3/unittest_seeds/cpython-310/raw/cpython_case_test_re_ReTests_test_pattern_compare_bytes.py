# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_pattern_compare_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern1 = re.compile(b'abc')
    re.purge()
    pattern2 = re.compile(b'abc')
    self.assertEqual(hash(pattern2), hash(pattern1))
    self.assertEqual(pattern2, pattern1)
    re.purge()
    pattern3 = re.compile('abc')
    with warnings.catch_warnings():
        warnings.simplefilter('error', BytesWarning)
        self.assertNotEqual(pattern3, pattern1)
