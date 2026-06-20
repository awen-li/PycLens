# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: RequestHandlerLoggingTestCase_test_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.con = http.client.HTTPConnection(self.HOST, self.PORT)
    self.con.connect()
    with support.captured_stderr() as err:
        self.con.request('GET', '/')
        self.con.getresponse()
    self.assertTrue(err.getvalue().endswith('"GET / HTTP/1.1" 200 -\n'))
