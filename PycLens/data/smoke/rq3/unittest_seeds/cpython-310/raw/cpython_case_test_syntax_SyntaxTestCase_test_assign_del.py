# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_assign_del

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_error('del (,)', 'invalid syntax')
    self._check_error('del 1', 'cannot delete literal')
    self._check_error('del (1, 2)', 'cannot delete literal')
    self._check_error('del None', 'cannot delete None')
    self._check_error('del *x', 'cannot delete starred')
    self._check_error('del (*x)', 'cannot use starred expression')
    self._check_error('del (*x,)', 'cannot delete starred')
    self._check_error('del [*x,]', 'cannot delete starred')
    self._check_error('del f()', 'cannot delete function call')
    self._check_error('del f(a, b)', 'cannot delete function call')
    self._check_error('del o.f()', 'cannot delete function call')
    self._check_error('del a[0]()', 'cannot delete function call')
    self._check_error('del x, f()', 'cannot delete function call')
    self._check_error('del f(), x', 'cannot delete function call')
    self._check_error('del [a, b, ((c), (d,), e.f())]', 'cannot delete function call')
    self._check_error('del (a if True else b)', 'cannot delete conditional')
    self._check_error('del +a', 'cannot delete expression')
    self._check_error('del a, +b', 'cannot delete expression')
    self._check_error('del a + b', 'cannot delete expression')
    self._check_error('del (a + b, c)', 'cannot delete expression')
    self._check_error('del (c[0], a + b)', 'cannot delete expression')
    self._check_error('del a.b.c + 2', 'cannot delete expression')
    self._check_error('del a.b.c[0] + 2', 'cannot delete expression')
    self._check_error('del (a, b, (c, d.e.f + 2))', 'cannot delete expression')
    self._check_error('del [a, b, (c, d.e.f[0] + 2)]', 'cannot delete expression')
    self._check_error('del (a := 5)', 'cannot delete named expression')
    self._check_error('del a += b', 'invalid syntax')
