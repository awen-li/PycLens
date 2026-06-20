# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_expressions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for expr in ('(x,)', '(x, y)', 'x := y', '(x := y)', 'x @y', '(x @ y)', 'x[0]', 'w[x].y.z', 'w + x - (y + z)', 'x(y)()(z)', '[w, x, y][z]', 'x.y'):
        compile(f'@{expr}\ndef f(): pass', 'test', 'exec')
