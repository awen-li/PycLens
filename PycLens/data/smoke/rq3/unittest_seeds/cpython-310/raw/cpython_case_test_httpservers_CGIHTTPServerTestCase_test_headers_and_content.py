# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_headers_and_content

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = self.request('/cgi-bin/file1.py')
    self.assertEqual((res.read(), res.getheader('Content-type'), res.status), (b'Hello World' + self.linesep, 'text/html', HTTPStatus.OK))
