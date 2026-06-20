# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_invaliduri

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = self.request('/cgi-bin/invalid')
    res.read()
    self.assertEqual(res.status, HTTPStatus.NOT_FOUND)
