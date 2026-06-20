# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_unicode_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class s1:

        def __repr__(self):
            return '\\n'

    class s2:

        def __repr__(self):
            return '\\n'
    self.assertEqual(repr(s1()), '\\n')
    self.assertEqual(repr(s2()), '\\n')
