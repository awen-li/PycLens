# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_ISO2022_test_iso2022_jp_g0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotIn(b'\x0e', '\xad'.encode('iso-2022-jp-2'))
    for encoding in ('iso-2022-jp-2004', 'iso-2022-jp-3'):
        e = '㐆'.encode(encoding)
        self.assertFalse(any((x > 128 for x in e)))
