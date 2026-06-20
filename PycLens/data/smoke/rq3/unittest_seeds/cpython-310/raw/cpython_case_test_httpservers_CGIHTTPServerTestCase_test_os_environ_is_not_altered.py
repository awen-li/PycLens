# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_os_environ_is_not_altered

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    signature = 'Test CGI Server'
    os.environ['SERVER_SOFTWARE'] = signature
    res = self.request('/cgi-bin/file1.py')
    self.assertEqual((b'Hello World' + self.linesep, 'text/html', HTTPStatus.OK), (res.read(), res.getheader('Content-type'), res.status))
    self.assertEqual(os.environ['SERVER_SOFTWARE'], signature)
