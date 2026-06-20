# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: MiscTests_test_gh_98778

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = urllib.error.HTTPError('url', 405, 'METHOD NOT ALLOWED', None, None)
    self.assertEqual(getattr(x, '__notes__', ()), ())
    self.assertIsInstance(x.fp.read(), bytes)
