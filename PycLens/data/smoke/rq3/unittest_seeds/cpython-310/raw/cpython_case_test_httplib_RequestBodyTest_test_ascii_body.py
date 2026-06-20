# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: RequestBodyTest_test_ascii_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.conn.request('PUT', '/url', 'body')
    (message, f) = self.get_headers_and_fp()
    self.assertEqual('text/plain', message.get_content_type())
    self.assertIsNone(message.get_charset())
    self.assertEqual('4', message.get('content-length'))
    self.assertEqual(b'body', f.read())
