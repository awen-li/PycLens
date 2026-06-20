# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_regular_templates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = Template('$who likes to eat a bag of $what worth $$100')
    self.assertEqual(s.substitute(dict(who='tim', what='ham')), 'tim likes to eat a bag of ham worth $100')
    self.assertRaises(KeyError, s.substitute, dict(who='tim'))
    self.assertRaises(TypeError, Template.substitute)
