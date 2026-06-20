# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_auto_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class HeaderCountingBuffer(list):

        def __init__(self):
            self.count = {}

        def append(self, item):
            kv = item.split(b':')
            if len(kv) > 1:
                lcKey = kv[0].decode('ascii').lower()
                self.count.setdefault(lcKey, 0)
                self.count[lcKey] += 1
            list.append(self, item)
    for explicit_header in (True, False):
        for header in ('Content-length', 'Host', 'Accept-encoding'):
            conn = client.HTTPConnection('example.com')
            conn.sock = FakeSocket('blahblahblah')
            conn._buffer = HeaderCountingBuffer()
            body = 'spamspamspam'
            headers = {}
            if explicit_header:
                headers[header] = str(len(body))
            conn.request('POST', '/', body, headers)
            self.assertEqual(conn._buffer.count[header.lower()], 1)
