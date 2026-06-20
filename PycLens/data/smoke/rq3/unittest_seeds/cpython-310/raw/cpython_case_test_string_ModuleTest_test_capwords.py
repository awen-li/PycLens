# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: ModuleTest_test_capwords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(string.capwords('abc def ghi'), 'Abc Def Ghi')
    self.assertEqual(string.capwords('abc\tdef\nghi'), 'Abc Def Ghi')
    self.assertEqual(string.capwords('abc\t   def  \nghi'), 'Abc Def Ghi')
    self.assertEqual(string.capwords('ABC DEF GHI'), 'Abc Def Ghi')
    self.assertEqual(string.capwords('ABC-DEF-GHI', '-'), 'Abc-Def-Ghi')
    self.assertEqual(string.capwords('ABC-def DEF-ghi GHI'), 'Abc-def Def-ghi Ghi')
    self.assertEqual(string.capwords('   aBc  DeF   '), 'Abc Def')
    self.assertEqual(string.capwords('\taBc\tDeF\t'), 'Abc Def')
    self.assertEqual(string.capwords('\taBc\tDeF\t', '\t'), '\tAbc\tDef\t')
