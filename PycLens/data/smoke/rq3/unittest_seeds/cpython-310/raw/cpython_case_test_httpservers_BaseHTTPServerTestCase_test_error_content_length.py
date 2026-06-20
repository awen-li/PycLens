# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_error_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con.request('NOTFOUND', '/')
    res = self.con.getresponse()
    self.assertEqual(res.status, HTTPStatus.NOT_FOUND)
    data = res.read()
    self.assertEqual(int(res.getheader('Content-Length')), len(data))
