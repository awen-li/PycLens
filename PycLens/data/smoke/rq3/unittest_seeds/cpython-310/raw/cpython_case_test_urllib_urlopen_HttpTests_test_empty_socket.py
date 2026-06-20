# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_HttpTests_test_empty_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.fakehttp(b'')
    try:
        self.assertRaises(OSError, urlopen, 'http://something')
    finally:
        self.unfakehttp()
