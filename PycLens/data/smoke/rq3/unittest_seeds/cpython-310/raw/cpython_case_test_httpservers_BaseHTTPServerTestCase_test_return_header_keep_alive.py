# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_return_header_keep_alive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con.request('KEEP', '/')
    res = self.con.getresponse()
    self.assertEqual(res.getheader('Connection'), 'keep-alive')
    self.con.request('TEST', '/')
    self.addCleanup(self.con.close)
