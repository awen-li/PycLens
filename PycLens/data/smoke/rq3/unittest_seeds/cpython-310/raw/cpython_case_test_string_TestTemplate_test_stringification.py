# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_stringification

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    s = Template('tim has eaten $count bags of ham today')
    d = dict(count=7)
    eq(s.substitute(d), 'tim has eaten 7 bags of ham today')
    eq(s.safe_substitute(d), 'tim has eaten 7 bags of ham today')
    s = Template('tim has eaten ${count} bags of ham today')
    eq(s.substitute(d), 'tim has eaten 7 bags of ham today')
