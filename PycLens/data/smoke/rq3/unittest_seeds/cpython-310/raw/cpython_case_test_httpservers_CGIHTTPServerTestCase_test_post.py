# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_post

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    params = urllib.parse.urlencode({'spam': 1, 'eggs': 'python', 'bacon': 123456})
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    res = self.request('/cgi-bin/file2.py', 'POST', params, headers)
    self.assertEqual(res.read(), b'1, python, 123456' + self.linesep)
