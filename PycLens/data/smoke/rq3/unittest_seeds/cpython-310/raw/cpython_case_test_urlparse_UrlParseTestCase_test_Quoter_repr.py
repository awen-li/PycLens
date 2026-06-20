# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_Quoter_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    quoter = urllib.parse.Quoter(urllib.parse._ALWAYS_SAFE)
    self.assertIn('Quoter', repr(quoter))
