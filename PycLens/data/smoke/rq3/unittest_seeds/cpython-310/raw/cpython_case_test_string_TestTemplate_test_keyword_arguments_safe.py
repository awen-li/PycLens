# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_keyword_arguments_safe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    raises = self.assertRaises
    s = Template('$who likes $what')
    eq(s.safe_substitute(who='tim', what='ham'), 'tim likes ham')
    eq(s.safe_substitute(dict(who='tim'), what='ham'), 'tim likes ham')
    eq(s.safe_substitute(dict(who='fred', what='kung pao'), who='tim', what='ham'), 'tim likes ham')
    s = Template('the mapping is $mapping')
    eq(s.safe_substitute(dict(foo='none'), mapping='bozo'), 'the mapping is bozo')
    eq(s.safe_substitute(dict(mapping='one'), mapping='two'), 'the mapping is two')
    d = dict(mapping='one')
    raises(TypeError, s.substitute, d, {})
    raises(TypeError, s.safe_substitute, d, {})
    s = Template('the self is $self')
    eq(s.safe_substitute(self='bozo'), 'the self is bozo')
