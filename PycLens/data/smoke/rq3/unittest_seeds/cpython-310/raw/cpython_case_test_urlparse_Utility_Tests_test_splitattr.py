# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splitattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitattr = urllib.parse._splitattr
    self.assertEqual(splitattr('/path;attr1=value1;attr2=value2'), ('/path', ['attr1=value1', 'attr2=value2']))
    self.assertEqual(splitattr('/path;'), ('/path', ['']))
    self.assertEqual(splitattr(';attr1=value1;attr2=value2'), ('', ['attr1=value1', 'attr2=value2']))
    self.assertEqual(splitattr('/path'), ('/path', []))
