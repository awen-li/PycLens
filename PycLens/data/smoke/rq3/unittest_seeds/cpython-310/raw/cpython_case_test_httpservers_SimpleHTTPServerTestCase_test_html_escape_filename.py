# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_html_escape_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = '<test&>.txt'
    fullpath = os.path.join(self.tempdir, filename)
    try:
        open(fullpath, 'wb').close()
    except OSError:
        raise unittest.SkipTest('Can not create file %s on current file system' % filename)
    try:
        response = self.request(self.base_url + '/')
        body = self.check_status_and_reason(response, HTTPStatus.OK)
        enc = response.headers.get_content_charset()
    finally:
        os.unlink(fullpath)
    self.assertIsNotNone(enc)
    html_text = '>%s<' % html.escape(filename, quote=False)
    self.assertIn(html_text.encode(enc), body)
