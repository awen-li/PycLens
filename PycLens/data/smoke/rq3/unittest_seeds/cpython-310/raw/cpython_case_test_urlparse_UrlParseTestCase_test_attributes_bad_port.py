# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_attributes_bad_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for bytes in (False, True):
        for parse in (urllib.parse.urlsplit, urllib.parse.urlparse):
            for port in ('foo', '1.5', '-1', '0x10', '-0', '1_1', ' 1', '1 ', '६'):
                with self.subTest(bytes=bytes, parse=parse, port=port):
                    netloc = 'www.example.net:' + port
                    url = 'http://' + netloc + '/'
                    if bytes:
                        if netloc.isascii() and port.isascii():
                            netloc = netloc.encode('ascii')
                            url = url.encode('ascii')
                        else:
                            continue
                    p = parse(url)
                    self.assertEqual(p.netloc, netloc)
                    with self.assertRaises(ValueError):
                        p.port
