# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_constructor_keyword_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(object='foo'), 'foo')
    self.assertEqual(str(object=b'foo', encoding='utf-8'), 'foo')
    self.assertEqual(str(b'foo', errors='strict'), 'foo')
    self.assertEqual(str(object=b'foo', errors='strict'), 'foo')
