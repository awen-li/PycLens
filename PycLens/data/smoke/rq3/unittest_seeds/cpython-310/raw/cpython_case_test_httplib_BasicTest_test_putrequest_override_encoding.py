# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_putrequest_override_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UnsafeHTTPConnection(client.HTTPConnection):

        def _encode_request(self, str_url):
            return str_url.encode('utf-8')
    conn = UnsafeHTTPConnection('example.com')
    conn.sock = FakeSocket('')
    conn.putrequest('GET', '/☃')
