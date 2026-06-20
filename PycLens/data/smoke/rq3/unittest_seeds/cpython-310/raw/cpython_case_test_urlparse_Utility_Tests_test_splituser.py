# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splituser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splituser = urllib.parse._splituser
    self.assertEqual(splituser('User:Pass@www.python.org:080'), ('User:Pass', 'www.python.org:080'))
    self.assertEqual(splituser('@www.python.org:080'), ('', 'www.python.org:080'))
    self.assertEqual(splituser('www.python.org:080'), (None, 'www.python.org:080'))
    self.assertEqual(splituser('User:Pass@'), ('User:Pass', ''))
    self.assertEqual(splituser('User@example.com:Pass@www.python.org:080'), ('User@example.com:Pass', 'www.python.org:080'))
