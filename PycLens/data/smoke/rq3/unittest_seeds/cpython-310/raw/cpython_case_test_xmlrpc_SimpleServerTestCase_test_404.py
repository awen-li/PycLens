# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_404

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with contextlib.closing(http.client.HTTPConnection(ADDR, PORT)) as conn:
        conn.request('POST', '/this-is-not-valid')
        response = conn.getresponse()
    self.assertEqual(response.status, 404)
    self.assertEqual(response.reason, 'Not Found')
