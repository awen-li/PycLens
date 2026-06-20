# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: ReprTests_test_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(r('abc'), "'abc'")
    eq(r('abcdefghijklmnop'), "'abcdefghijklmnop'")
    s = 'a' * 30 + 'b' * 30
    expected = repr(s)[:13] + '...' + repr(s)[-14:]
    eq(r(s), expected)
    eq(r('"\''), repr('"\''))
    s = '"' * 30 + "'" * 100
    expected = repr(s)[:13] + '...' + repr(s)[-14:]
    eq(r(s), expected)
