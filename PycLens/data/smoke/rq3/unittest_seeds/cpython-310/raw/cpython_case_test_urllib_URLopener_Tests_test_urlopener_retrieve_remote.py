# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: URLopener_Tests_test_urlopener_retrieve_remote

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = 'http://www.python.org/file.txt'
    self.fakehttp(b'HTTP/1.1 200 OK\r\n\r\nHello!')
    self.addCleanup(self.unfakehttp)
    (filename, _) = urllib.request.URLopener().retrieve(url)
    self.assertEqual(os.path.splitext(filename)[1], '.txt')
