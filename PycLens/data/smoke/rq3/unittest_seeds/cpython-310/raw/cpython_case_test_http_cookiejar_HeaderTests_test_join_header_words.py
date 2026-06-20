# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookiejar.py
# case: HeaderTests_test_join_header_words

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    joined = join_header_words([[('foo', None), ('bar', 'baz')]])
    self.assertEqual(joined, 'foo; bar=baz')
    self.assertEqual(join_header_words([[]]), '')
