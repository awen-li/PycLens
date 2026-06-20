# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_format_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class S(str):

        def __str__(self):
            return '__str__ overridden'
    s = S('xxx')
    self.assertEqual('%s' % s, '__str__ overridden')
    self.assertEqual('{}'.format(s), '__str__ overridden')
