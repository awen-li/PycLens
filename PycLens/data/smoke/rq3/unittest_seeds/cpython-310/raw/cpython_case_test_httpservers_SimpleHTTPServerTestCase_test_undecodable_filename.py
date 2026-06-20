# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_undecodable_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    enc = sys.getfilesystemencoding()
    filename = os.fsdecode(os_helper.TESTFN_UNDECODABLE) + '.txt'
    with open(os.path.join(self.tempdir, filename), 'wb') as f:
        f.write(os_helper.TESTFN_UNDECODABLE)
    response = self.request(self.base_url + '/')
    if sys.platform == 'darwin':
        for name in os.listdir(self.tempdir):
            if name != 'test':
                filename = name
                break
    body = self.check_status_and_reason(response, HTTPStatus.OK)
    quotedname = urllib.parse.quote(filename, errors='surrogatepass')
    self.assertIn(('href="%s"' % quotedname).encode(enc, 'surrogateescape'), body)
    self.assertIn(('>%s<' % html.escape(filename, quote=False)).encode(enc, 'surrogateescape'), body)
    response = self.request(self.base_url + '/' + quotedname)
    self.check_status_and_reason(response, HTTPStatus.OK, data=os_helper.TESTFN_UNDECODABLE)
