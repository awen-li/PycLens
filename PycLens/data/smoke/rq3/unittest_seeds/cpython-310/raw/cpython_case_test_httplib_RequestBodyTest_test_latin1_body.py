# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: RequestBodyTest_test_latin1_body

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.conn.request('PUT', '/url', 'bodyÁ')
    (message, f) = self.get_headers_and_fp()
    self.assertEqual('text/plain', message.get_content_type())
    self.assertIsNone(message.get_charset())
    self.assertEqual('5', message.get('content-length'))
    self.assertEqual(b'body\xc1', f.read())
