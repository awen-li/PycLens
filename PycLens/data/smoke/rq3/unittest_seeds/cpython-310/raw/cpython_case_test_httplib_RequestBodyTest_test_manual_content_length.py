# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: RequestBodyTest_test_manual_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.conn.request('PUT', '/url', 'body', {'Content-Length': '42'})
    (message, f) = self.get_headers_and_fp()
    self.assertEqual('42', message.get('content-length'))
    self.assertEqual(4, len(f.read()))
