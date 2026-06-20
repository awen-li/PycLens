# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_willclose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakehttp(b'HTTP/1.1 200 OK\r\n\r\nHello!')
    try:
        resp = urlopen('http://www.python.org')
        self.assertTrue(resp.fp.will_close)
    finally:
        self.unfakehttp()
