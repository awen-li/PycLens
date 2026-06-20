# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: CGIHandlerTestCase_test_cgi_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env['REQUEST_METHOD'] = 'GET'
        with captured_stdout(encoding=self.cgi.encoding) as data_out:
            self.cgi.handle_request()
        data_out.seek(0)
        handle = data_out.read()
        status = handle.split()[1]
        message = ' '.join(handle.split()[2:4])
        self.assertEqual(status, '400')
        self.assertEqual(message, 'Bad Request')
