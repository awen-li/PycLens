# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: WrapTestCase_test_funky_parens

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_split('foo (--option) bar', ['foo', ' ', '(--option)', ' ', 'bar'])
    self.check_split('foo (bar) baz', ['foo', ' ', '(bar)', ' ', 'baz'])
    self.check_split('blah (ding dong), wubba', ['blah', ' ', '(ding', ' ', 'dong),', ' ', 'wubba'])
