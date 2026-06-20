# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_ar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    f = gettext.c2py('n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 ? 4 : 5')
    s = ''.join([str(f(x)) for x in range(200)])
    eq(s, '01233333333444444444444444444444444444444444444444444444444444444444444444444444444444444444444444445553333333344444444444444444444444444444444444444444444444444444444444444444444444444444444444444444')
