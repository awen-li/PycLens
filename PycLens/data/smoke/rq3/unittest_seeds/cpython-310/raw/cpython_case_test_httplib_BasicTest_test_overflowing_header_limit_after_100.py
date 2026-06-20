# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_overflowing_header_limit_after_100

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 100 OK\r\nr\n' * 32768
    resp = client.HTTPResponse(FakeSocket(body))
    with self.assertRaises(client.HTTPException) as cm:
        resp.begin()
    self.assertIn('got more than ', str(cm.exception))
    self.assertIn('headers', str(cm.exception))
