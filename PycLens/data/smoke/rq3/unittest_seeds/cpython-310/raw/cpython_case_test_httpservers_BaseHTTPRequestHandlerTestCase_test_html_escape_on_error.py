# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_html_escape_on_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.send_typical_request(b'<script>alert("hello")</script> / HTTP/1.1')
    result = b''.join(result)
    text = '<script>alert("hello")</script>'
    self.assertIn(html.escape(text, quote=False).encode('ascii'), result)
