# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splithost

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splithost = urllib.parse._splithost
    self.assertEqual(splithost('//www.example.org:80/foo/bar/baz.html'), ('www.example.org:80', '/foo/bar/baz.html'))
    self.assertEqual(splithost('//www.example.org:80'), ('www.example.org:80', ''))
    self.assertEqual(splithost('/foo/bar/baz.html'), (None, '/foo/bar/baz.html'))
    self.assertEqual(splithost('//127.0.0.1#@host.com'), ('127.0.0.1', '/#@host.com'))
    self.assertEqual(splithost('//127.0.0.1#@host.com:80'), ('127.0.0.1', '/#@host.com:80'))
    self.assertEqual(splithost('//127.0.0.1:80#@host.com'), ('127.0.0.1:80', '/#@host.com'))
    self.assertEqual(splithost('///file'), ('', '/file'))
    self.assertEqual(splithost('//example.net/file;'), ('example.net', '/file;'))
    self.assertEqual(splithost('//example.net/file?'), ('example.net', '/file?'))
    self.assertEqual(splithost('//example.net/file#'), ('example.net', '/file#'))
