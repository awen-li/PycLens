# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_url_host_with_control_char_rejected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for char_no in list(range(0, 33)) + [127]:
        char = chr(char_no)
        schemeless_url = f'//localhost{char}/test/'
        self.fakehttp(b'HTTP/1.1 200 OK\r\n\r\nHello.')
        try:
            escaped_char_repr = repr(char).replace('\\', '\\\\')
            InvalidURL = http.client.InvalidURL
            with self.assertRaisesRegex(InvalidURL, f'contain control.*{escaped_char_repr}'):
                urlopen(f'http:{schemeless_url}')
            with self.assertRaisesRegex(InvalidURL, f'contain control.*{escaped_char_repr}'):
                urlopen(f'https:{schemeless_url}')
        finally:
            self.unfakehttp()
