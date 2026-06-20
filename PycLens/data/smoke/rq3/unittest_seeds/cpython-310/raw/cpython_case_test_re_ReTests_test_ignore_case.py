# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_ignore_case

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('abc', 'ABC', re.I).group(0), 'ABC')
    self.assertEqual(re.match(b'abc', b'ABC', re.I).group(0), b'ABC')
    self.assertEqual(re.match('(a\\s[^a])', 'a b', re.I).group(1), 'a b')
    self.assertEqual(re.match('(a\\s[^a]*)', 'a bb', re.I).group(1), 'a bb')
    self.assertEqual(re.match('(a\\s[abc])', 'a b', re.I).group(1), 'a b')
    self.assertEqual(re.match('(a\\s[abc]*)', 'a bb', re.I).group(1), 'a bb')
    self.assertEqual(re.match('((a)\\s\\2)', 'a a', re.I).group(1), 'a a')
    self.assertEqual(re.match('((a)\\s\\2*)', 'a aa', re.I).group(1), 'a aa')
    self.assertEqual(re.match('((a)\\s(abc|a))', 'a a', re.I).group(1), 'a a')
    self.assertEqual(re.match('((a)\\s(abc|a)*)', 'a aa', re.I).group(1), 'a aa')
    assert 'K'.lower() == 'K'.lower() == 'k'
    self.assertTrue(re.match('K', 'K', re.I))
    self.assertTrue(re.match('k', 'K', re.I))
    self.assertTrue(re.match('\\u212a', 'K', re.I))
    self.assertTrue(re.match('\\u212a', 'k', re.I))
    assert 's'.upper() == 'ſ'.upper() == 'S'
    self.assertTrue(re.match('S', 'ſ', re.I))
    self.assertTrue(re.match('s', 'ſ', re.I))
    self.assertTrue(re.match('\\u017f', 'S', re.I))
    self.assertTrue(re.match('\\u017f', 's', re.I))
    assert 'в'.upper() == 'ᲀ'.upper() == 'В'
    self.assertTrue(re.match('\\u0412', 'в', re.I))
    self.assertTrue(re.match('\\u0412', 'ᲀ', re.I))
    self.assertTrue(re.match('\\u0432', 'В', re.I))
    self.assertTrue(re.match('\\u0432', 'ᲀ', re.I))
    self.assertTrue(re.match('\\u1c80', 'В', re.I))
    self.assertTrue(re.match('\\u1c80', 'в', re.I))
    assert 'ﬅ'.upper() == 'ﬆ'.upper() == 'ST'
    self.assertTrue(re.match('\\ufb05', 'ﬆ', re.I))
    self.assertTrue(re.match('\\ufb06', 'ﬅ', re.I))
