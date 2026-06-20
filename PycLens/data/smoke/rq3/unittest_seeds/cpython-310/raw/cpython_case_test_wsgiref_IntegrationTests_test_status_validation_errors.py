# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_status_validation_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def create_bad_app(status):

        def bad_app(environ, start_response):
            start_response(status, [('Content-Type', 'text/plain; charset=utf-8')])
            return [b'Hello, world!']
        return bad_app
    tests = [('200', 'AssertionError: Status must be at least 4 characters'), ('20X OK', 'AssertionError: Status message must begin w/3-digit code'), ('200OK', 'AssertionError: Status message must have a space after code')]
    for (status, exc_message) in tests:
        with self.subTest(status=status):
            (out, err) = run_amock(create_bad_app(status))
            self.assertTrue(out.endswith(b'A server error occurred.  Please contact the administrator.'))
            self.assertEqual(err.splitlines()[-2], exc_message)
