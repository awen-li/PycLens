# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userstring.py
# case: UserStringTest_test_rmod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ustr2(UserString):
        pass

    class ustr3(ustr2):

        def __rmod__(self, other):
            return super().__rmod__(other)
    fmt2 = ustr2('value is %s')
    str3 = ustr3('TEST')
    self.assertEqual(fmt2 % str3, 'value is TEST')
