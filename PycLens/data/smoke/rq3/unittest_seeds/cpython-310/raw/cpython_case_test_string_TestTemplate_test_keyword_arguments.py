# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_keyword_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    s = Template('$who likes $what')
    eq(s.substitute(who='tim', what='ham'), 'tim likes ham')
    eq(s.substitute(dict(who='tim'), what='ham'), 'tim likes ham')
    eq(s.substitute(dict(who='fred', what='kung pao'), who='tim', what='ham'), 'tim likes ham')
    s = Template('the mapping is $mapping')
    eq(s.substitute(dict(foo='none'), mapping='bozo'), 'the mapping is bozo')
    eq(s.substitute(dict(mapping='one'), mapping='two'), 'the mapping is two')
    s = Template('the self is $self')
    eq(s.substitute(self='bozo'), 'the self is bozo')
