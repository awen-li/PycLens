# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_version_none_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con._http_vsn_str = ''
    self.con.putrequest('GET', '/')
    self.con.endheaders()
    res = self.con.getresponse()
    self.assertEqual(res.status, HTTPStatus.NOT_IMPLEMENTED)
