# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_authorization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    headers = {b'Authorization': b'Basic ' + base64.b64encode(b'username:pass')}
    res = self.request('/cgi-bin/file1.py', 'GET', headers=headers)
    self.assertEqual((b'Hello World' + self.linesep, 'text/html', HTTPStatus.OK), (res.read(), res.getheader('Content-type'), res.status))
