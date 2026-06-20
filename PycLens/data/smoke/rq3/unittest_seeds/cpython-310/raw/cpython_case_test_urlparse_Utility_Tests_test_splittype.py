# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splittype

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splittype = urllib.parse._splittype
    self.assertEqual(splittype('type:opaquestring'), ('type', 'opaquestring'))
    self.assertEqual(splittype('opaquestring'), (None, 'opaquestring'))
    self.assertEqual(splittype(':opaquestring'), (None, ':opaquestring'))
    self.assertEqual(splittype('type:'), ('type', ''))
    self.assertEqual(splittype('type:opaque:string'), ('type', 'opaque:string'))
