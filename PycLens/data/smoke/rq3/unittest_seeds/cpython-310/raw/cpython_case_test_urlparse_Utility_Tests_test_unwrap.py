# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_unwrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for wrapped_url in ('<URL:scheme://host/path>', '<scheme://host/path>', 'URL:scheme://host/path', 'scheme://host/path'):
        url = urllib.parse.unwrap(wrapped_url)
        self.assertEqual(url, 'scheme://host/path')
