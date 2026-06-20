# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_cgi_path_in_sub_directories

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        CGIHTTPRequestHandler.cgi_directories.append('/sub/dir/cgi-bin')
        res = self.request('/sub/dir/cgi-bin/file5.py')
        self.assertEqual((b'Hello World' + self.linesep, 'text/html', HTTPStatus.OK), (res.read(), res.getheader('Content-type'), res.status))
    finally:
        CGIHTTPRequestHandler.cgi_directories.remove('/sub/dir/cgi-bin')
