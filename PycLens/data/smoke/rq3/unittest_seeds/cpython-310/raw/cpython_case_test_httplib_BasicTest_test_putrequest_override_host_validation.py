# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_putrequest_override_host_validation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UnsafeHTTPConnection(client.HTTPConnection):

        def _validate_host(self, url):
            pass
    conn = UnsafeHTTPConnection('example.com\r\n')
    conn.sock = FakeSocket('')
    conn.putrequest('GET', '/', skip_host=1)
