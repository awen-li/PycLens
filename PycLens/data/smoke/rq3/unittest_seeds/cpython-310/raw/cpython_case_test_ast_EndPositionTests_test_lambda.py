# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_lambda

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'lambda x, *y: None'
    lam = self._parse_value(s)
    self._check_content(s, lam.body, 'None')
    self._check_content(s, lam.args.args[0], 'x')
    self._check_content(s, lam.args.vararg, 'y')
