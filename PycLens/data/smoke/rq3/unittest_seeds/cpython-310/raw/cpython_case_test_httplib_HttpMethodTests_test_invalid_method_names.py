# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HttpMethodTests_test_invalid_method_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    methods = ('GET\r', 'POST\n', 'PUT\n\r', 'POST\nValue', 'POST\nHOST:abc', 'GET\nrHost:abc\n', 'POST\rRemainder:\r', 'GET\rHOST:\n', '\nPUT')
    for method in methods:
        with self.assertRaisesRegex(ValueError, "method can't contain control characters"):
            conn = client.HTTPConnection('example.com')
            conn.sock = FakeSocket(None)
            conn.request(method=method, url='/')
