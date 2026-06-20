# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_content_length_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ContentLengthChecker(list):

        def __init__(self):
            list.__init__(self)
            self.content_length = None

        def append(self, item):
            kv = item.split(b':', 1)
            if len(kv) > 1 and kv[0].lower() == b'content-length':
                self.content_length = kv[1].strip()
            list.append(self, item)
    bodies = (None, '')
    methods_with_body = ('PUT', 'POST', 'PATCH')
    for (method, body) in itertools.product(methods_with_body, bodies):
        conn = client.HTTPConnection('example.com')
        conn.sock = FakeSocket(None)
        conn._buffer = ContentLengthChecker()
        conn.request(method, '/', body)
        self.assertEqual(conn._buffer.content_length, b'0', 'Header Content-Length incorrect on {}'.format(method))
    methods_without_body = ('GET', 'CONNECT', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE')
    for method in methods_without_body:
        conn = client.HTTPConnection('example.com')
        conn.sock = FakeSocket(None)
        conn._buffer = ContentLengthChecker()
        conn.request(method, '/', None)
        self.assertEqual(conn._buffer.content_length, None, 'Header Content-Length set for empty body on {}'.format(method))
    for method in methods_without_body:
        conn = client.HTTPConnection('example.com')
        conn.sock = FakeSocket(None)
        conn._buffer = ContentLengthChecker()
        conn.request(method, '/', '')
        self.assertEqual(conn._buffer.content_length, b'0', 'Header Content-Length incorrect on {}'.format(method))
    for method in itertools.chain(methods_without_body, methods_with_body):
        conn = client.HTTPConnection('example.com')
        conn.sock = FakeSocket(None)
        conn._buffer = ContentLengthChecker()
        conn.request(method, '/', ' ')
        self.assertEqual(conn._buffer.content_length, b'1', 'Header Content-Length incorrect on {}'.format(method))
