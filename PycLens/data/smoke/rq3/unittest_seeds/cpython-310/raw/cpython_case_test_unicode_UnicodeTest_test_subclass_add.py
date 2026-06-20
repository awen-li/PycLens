# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_subclass_add

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class S(str):

        def __add__(self, o):
            return '3'
    self.assertEqual(S('4') + S('5'), '3')

    class S(str):

        def __iadd__(self, o):
            return '3'
    s = S('1')
    s += '4'
    self.assertEqual(s, '3')
