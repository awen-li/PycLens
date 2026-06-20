# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_url_host_with_newline_header_injection_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakehttp(b'HTTP/1.1 200 OK\r\n\r\nHello.')
    host = 'localhost\r\nX-injected: header\r\n'
    schemeless_url = '//' + host + ':8080/test/?test=a'
    try:
        InvalidURL = http.client.InvalidURL
        with self.assertRaisesRegex(InvalidURL, 'contain control.*\\\\r'):
            urlopen(f'http:{schemeless_url}')
        with self.assertRaisesRegex(InvalidURL, 'contain control.*\\\\n'):
            urlopen(f'https:{schemeless_url}')
    finally:
        self.unfakehttp()
