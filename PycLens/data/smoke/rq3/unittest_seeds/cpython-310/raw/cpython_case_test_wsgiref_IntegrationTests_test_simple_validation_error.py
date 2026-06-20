# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_simple_validation_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def bad_app(environ, start_response):
        start_response('200 OK', ('Content-Type', 'text/plain'))
        return ['Hello, world!']
    (out, err) = run_amock(validator(bad_app))
    self.assertTrue(out.endswith(b'A server error occurred.  Please contact the administrator.'))
    self.assertEqual(err.splitlines()[-2], "AssertionError: Headers (('Content-Type', 'text/plain')) must be of type list: <class 'tuple'>")
