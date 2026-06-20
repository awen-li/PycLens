# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_userpass_inurl_w_spaces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakehttp(b'HTTP/1.0 200 OK\r\n\r\nHello!')
    try:
        userpass = 'a b:c d'
        url = 'http://{}@python.org/'.format(userpass)
        fakehttp_wrapper = http.client.HTTPConnection
        authorization = 'Authorization: Basic %s\r\n' % b64encode(userpass.encode('ASCII')).decode('ASCII')
        fp = urlopen(url)
        self.assertIn(authorization, fakehttp_wrapper.buf.decode('UTF-8'))
        self.assertEqual(fp.readline(), b'Hello!')
        self.assertEqual(fp.readline(), b'')
        self.assertNotEqual(fp.geturl(), url)
        self.assertEqual(fp.getcode(), 200)
    finally:
        self.unfakehttp()
