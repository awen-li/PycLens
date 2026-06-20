# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_header_keep_alive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con._http_vsn_str = 'HTTP/1.1'
    self.con.putrequest('GET', '/')
    self.con.putheader('Connection', 'keep-alive')
    self.con.endheaders()
    res = self.con.getresponse()
    self.assertEqual(res.status, HTTPStatus.NOT_IMPLEMENTED)
