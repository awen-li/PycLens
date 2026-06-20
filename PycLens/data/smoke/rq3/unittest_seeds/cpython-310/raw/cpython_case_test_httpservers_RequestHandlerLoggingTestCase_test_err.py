# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: RequestHandlerLoggingTestCase_test_err

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con = http.client.HTTPConnection(self.HOST, self.PORT)
    self.con.connect()
    with support.captured_stderr() as err:
        self.con.request('ERROR', '/')
        self.con.getresponse()
    lines = err.getvalue().split('\n')
    self.assertTrue(lines[0].endswith('code 404, message File not found'))
    self.assertTrue(lines[1].endswith('"ERROR / HTTP/1.1" 404 -'))
