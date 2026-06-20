# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_version_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con._http_vsn = 99
    self.con._http_vsn_str = 'HTTP/9.9'
    self.con.putrequest('GET', '/')
    self.con.endheaders()
    res = self.con.getresponse()
    self.assertEqual(res.status, HTTPStatus.HTTP_VERSION_NOT_SUPPORTED)
