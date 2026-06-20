# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splitpasswd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitpasswd = urllib.parse._splitpasswd
    self.assertEqual(splitpasswd('user:ab'), ('user', 'ab'))
    self.assertEqual(splitpasswd('user:a\nb'), ('user', 'a\nb'))
    self.assertEqual(splitpasswd('user:a\tb'), ('user', 'a\tb'))
    self.assertEqual(splitpasswd('user:a\rb'), ('user', 'a\rb'))
    self.assertEqual(splitpasswd('user:a\x0cb'), ('user', 'a\x0cb'))
    self.assertEqual(splitpasswd('user:a\x0bb'), ('user', 'a\x0bb'))
    self.assertEqual(splitpasswd('user:a:b'), ('user', 'a:b'))
    self.assertEqual(splitpasswd('user:a b'), ('user', 'a b'))
    self.assertEqual(splitpasswd('user 2:ab'), ('user 2', 'ab'))
    self.assertEqual(splitpasswd('user+1:a+b'), ('user+1', 'a+b'))
    self.assertEqual(splitpasswd('user:'), ('user', ''))
    self.assertEqual(splitpasswd('user'), ('user', None))
    self.assertEqual(splitpasswd(':ab'), ('', 'ab'))
