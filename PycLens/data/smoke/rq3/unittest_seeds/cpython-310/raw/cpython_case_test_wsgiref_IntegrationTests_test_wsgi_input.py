# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_wsgi_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def bad_app(e, s):
        e['wsgi.input'].read()
        s('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
        return [b'data']
    (out, err) = run_amock(validator(bad_app))
    self.assertTrue(out.endswith(b'A server error occurred.  Please contact the administrator.'))
    self.assertEqual(err.splitlines()[-2], 'AssertionError')
