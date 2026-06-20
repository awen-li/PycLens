# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_request_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (out, err) = run_amock(data=b'GET ' + b'x' * 65537 + b' HTTP/1.0\n\n')
    self.assertEqual(out.splitlines()[0], b'HTTP/1.0 414 Request-URI Too Long')
