# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_escapes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    s = Template('$who likes to eat a bag of $$what worth $$100')
    eq(s.substitute(dict(who='tim', what='ham')), 'tim likes to eat a bag of $what worth $100')
    s = Template('$who likes $$')
    eq(s.substitute(dict(who='tim', what='ham')), 'tim likes $')
