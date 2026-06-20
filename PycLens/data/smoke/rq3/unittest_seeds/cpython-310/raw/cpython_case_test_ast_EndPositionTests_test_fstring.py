# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_fstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'x = f"abc {x + y} abc"'
    fstr = self._parse_value(s)
    binop = fstr.values[1].value
    self._check_content(s, binop, 'x + y')
