# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: RequestBodyTest_test_binary_file_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'wb') as f:
        f.write(b'body\xc1')
    with open(os_helper.TESTFN, 'rb') as f:
        self.conn.request('PUT', '/url', f)
        (message, f) = self.get_headers_and_fp()
        self.assertEqual('text/plain', message.get_content_type())
        self.assertIsNone(message.get_charset())
        self.assertEqual('chunked', message.get('Transfer-Encoding'))
        self.assertNotIn('Content-Length', message)
        self.assertEqual(b'5\r\nbody\xc1\r\n0\r\n\r\n', f.read())
