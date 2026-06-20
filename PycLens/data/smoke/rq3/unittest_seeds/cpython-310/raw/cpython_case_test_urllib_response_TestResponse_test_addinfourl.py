# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib_response.py
# case: TestResponse_test_addinfourl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = 'http://www.python.org'
    code = 200
    infourl = urllib.response.addinfourl(self.fp, self.test_headers, url, code)
    self.assertEqual(infourl.info(), self.test_headers)
    self.assertEqual(infourl.geturl(), url)
    self.assertEqual(infourl.getcode(), code)
    self.assertEqual(infourl.headers, self.test_headers)
    self.assertEqual(infourl.url, url)
    self.assertEqual(infourl.status, code)
