# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_delimiter_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    raises = self.assertRaises

    class AmpersandTemplate(Template):
        delimiter = '&'
    s = AmpersandTemplate('this &gift is for &{who} &&')
    eq(s.substitute(gift='bud', who='you'), 'this bud is for you &')
    raises(KeyError, s.substitute)
    eq(s.safe_substitute(gift='bud', who='you'), 'this bud is for you &')
    eq(s.safe_substitute(), 'this &gift is for &{who} &')
    s = AmpersandTemplate('this &gift is for &{who} &')
    raises(ValueError, s.substitute, dict(gift='bud', who='you'))
    eq(s.safe_substitute(), 'this &gift is for &{who} &')

    class PieDelims(Template):
        delimiter = '@'
    s = PieDelims('@who likes to eat a bag of @{what} worth $100')
    self.assertEqual(s.substitute(dict(who='tim', what='ham')), 'tim likes to eat a bag of ham worth $100')
