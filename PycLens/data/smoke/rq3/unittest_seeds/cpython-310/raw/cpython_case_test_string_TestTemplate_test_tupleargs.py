# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_tupleargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    s = Template('$who ate ${meal}')
    d = dict(who=('tim', 'fred'), meal=('ham', 'kung pao'))
    eq(s.substitute(d), "('tim', 'fred') ate ('ham', 'kung pao')")
    eq(s.safe_substitute(d), "('tim', 'fred') ate ('ham', 'kung pao')")
