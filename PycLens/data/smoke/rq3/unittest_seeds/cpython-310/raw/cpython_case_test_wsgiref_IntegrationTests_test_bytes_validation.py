# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_bytes_validation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def app(e, s):
        s('200 OK', [('Content-Type', 'text/plain; charset=utf-8'), ('Date', 'Wed, 24 Dec 2008 13:29:32 GMT')])
        return [b'data']
    (out, err) = run_amock(validator(app))
    self.assertTrue(err.endswith('"GET / HTTP/1.0" 200 4\n'))
    ver = sys.version.split()[0].encode('ascii')
    py = python_implementation().encode('ascii')
    pyver = py + b'/' + ver
    self.assertEqual(b'HTTP/1.0 200 OK\r\nServer: WSGIServer/0.2 ' + pyver + b'\r\nContent-Type: text/plain; charset=utf-8\r\nDate: Wed, 24 Dec 2008 13:29:32 GMT\r\n\r\ndata', out)
