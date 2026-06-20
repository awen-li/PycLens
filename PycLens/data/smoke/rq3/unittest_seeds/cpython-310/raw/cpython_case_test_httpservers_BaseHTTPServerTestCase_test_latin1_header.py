# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_latin1_header

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con.request('LATINONEHEADER', '/', headers={'X-Special-Incoming': 'Ärger mit Unicode'})
    res = self.con.getresponse()
    self.assertEqual(res.getheader('X-Special'), 'Dängerous Mind')
    self.assertEqual(res.read(), 'Ärger mit Unicode'.encode('utf-8'))
