# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestMisc_test_decistmt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from decimal import Decimal
    s = '+21.3e-5*-.1234/81.7'
    self.assertEqual(decistmt(s), "+Decimal ('21.3e-5')*-Decimal ('.1234')/Decimal ('81.7')")
    self.assertRegex(repr(eval(s)), '-3.2171603427[0-9]*e-0+7')
    self.assertEqual(eval(decistmt(s)), Decimal('-3.217160342717258261933904529E-7'))
