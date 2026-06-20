# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'func(x, y=2, **kw)'
    call = self._parse_value(s)
    self._check_content(s, call.func, 'func')
    self._check_content(s, call.keywords[0].value, '2')
    self._check_content(s, call.keywords[1].value, 'kw')
