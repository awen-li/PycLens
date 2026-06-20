# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: SurrogateEscapeTest_test_latin1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('\udce4\udceb\udcef\udcf6\udcfc'.encode('latin-1', 'surrogateescape'), b'\xe4\xeb\xef\xf6\xfc')
