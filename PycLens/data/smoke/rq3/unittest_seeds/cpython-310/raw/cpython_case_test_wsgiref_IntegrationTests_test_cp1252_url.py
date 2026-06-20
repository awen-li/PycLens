# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_cp1252_url

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def app(e, s):
        s('200 OK', [('Content-Type', 'text/plain'), ('Date', 'Wed, 24 Dec 2008 13:29:32 GMT')])
        return [e['PATH_INFO'].encode('latin1')]
    (out, err) = run_amock(validator(app), data=b'GET /\x80%80 HTTP/1.0')
    self.assertEqual([b'HTTP/1.0 200 OK', mock.ANY, b'Content-Type: text/plain', b'Date: Wed, 24 Dec 2008 13:29:32 GMT', b'', b'/\x80\x80'], out.splitlines())
