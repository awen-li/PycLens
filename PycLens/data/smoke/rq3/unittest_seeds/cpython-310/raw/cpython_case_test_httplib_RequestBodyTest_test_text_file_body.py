# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: RequestBodyTest_test_text_file_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'w', encoding='utf-8') as f:
        f.write('body')
    with open(os_helper.TESTFN, encoding='utf-8') as f:
        self.conn.request('PUT', '/url', f)
        (message, f) = self.get_headers_and_fp()
        self.assertEqual('text/plain', message.get_content_type())
        self.assertIsNone(message.get_charset())
        self.assertIsNone(message.get('content-length'))
        self.assertEqual('chunked', message.get('transfer-encoding'))
        self.assertEqual(b'4\r\nbody\r\n0\r\n\r\n', f.read())
