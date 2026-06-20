# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: DeprecationTest_test_splittag_deprecation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertWarns(DeprecationWarning) as cm:
        urllib.parse.splittag('')
    self.assertEqual(str(cm.warning), 'urllib.parse.splittag() is deprecated as of 3.8, use urllib.parse.urlparse() instead')
