# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_string.py
# case: TestTemplate_test_percents

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    s = Template('%(foo)s $foo ${foo}')
    d = dict(foo='baz')
    eq(s.substitute(d), '%(foo)s baz baz')
    eq(s.safe_substitute(d), '%(foo)s baz baz')
