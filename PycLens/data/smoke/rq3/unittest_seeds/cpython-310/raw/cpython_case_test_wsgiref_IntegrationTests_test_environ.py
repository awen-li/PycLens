# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_environ

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    request = b'GET /p%61th/?query=test HTTP/1.0\nX-Test-Header: Python test \nX-Test-Header: Python test 2\nContent-Length: 0\n\n'
    (out, err) = run_amock(header_app, request)
    self.assertEqual(out.splitlines()[-1], b'Python test,Python test 2;query=test;/path/')
