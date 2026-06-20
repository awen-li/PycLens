# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_return_explain_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con.request('EXPLAINERROR', '/')
    res = self.con.getresponse()
    self.assertEqual(res.status, 999)
    self.assertTrue(int(res.getheader('Content-Length')))
