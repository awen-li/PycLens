# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_overflowing_status_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = 'HTTP/1.1 200 Ok' + 'k' * 65536 + '\r\n'
    resp = client.HTTPResponse(FakeSocket(body))
    self.assertRaises((client.LineTooLong, client.BadStatusLine), resp.begin)
