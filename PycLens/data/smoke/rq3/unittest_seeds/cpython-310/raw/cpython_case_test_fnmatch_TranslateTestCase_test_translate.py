# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fnmatch.py
# case: TranslateTestCase_test_translate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import re
    self.assertEqual(translate('*'), '(?s:.*)\\Z')
    self.assertEqual(translate('?'), '(?s:.)\\Z')
    self.assertEqual(translate('a?b*'), '(?s:a.b.*)\\Z')
    self.assertEqual(translate('[abc]'), '(?s:[abc])\\Z')
    self.assertEqual(translate('[]]'), '(?s:[]])\\Z')
    self.assertEqual(translate('[!x]'), '(?s:[^x])\\Z')
    self.assertEqual(translate('[^x]'), '(?s:[\\^x])\\Z')
    self.assertEqual(translate('[x'), '(?s:\\[x)\\Z')
    self.assertEqual(translate('*.txt'), '(?s:.*\\.txt)\\Z')
    self.assertEqual(translate('*********'), '(?s:.*)\\Z')
    self.assertEqual(translate('A*********'), '(?s:A.*)\\Z')
    self.assertEqual(translate('*********A'), '(?s:.*A)\\Z')
    self.assertEqual(translate('A*********?[?]?'), '(?s:A.*.[?].)\\Z')
    t = translate('**a*a****a')
    digits = re.findall('\\d+', t)
    self.assertEqual(len(digits), 4)
    self.assertEqual(digits[0], digits[1])
    self.assertEqual(digits[2], digits[3])
    g1 = f'g{digits[0]}'
    g2 = f'g{digits[2]}'
    self.assertEqual(t, f'(?s:(?=(?P<{g1}>.*?a))(?P={g1})(?=(?P<{g2}>.*?a))(?P={g2}).*a)\\Z')
    r1 = translate('**a**a**a*')
    r2 = translate('**b**b**b*')
    r3 = translate('*c*c*c*')
    fatre = '|'.join([r1, r2, r3])
    self.assertTrue(re.match(fatre, 'abaccad'))
    self.assertTrue(re.match(fatre, 'abxbcab'))
    self.assertTrue(re.match(fatre, 'cbabcaxc'))
    self.assertFalse(re.match(fatre, 'dabccbad'))
