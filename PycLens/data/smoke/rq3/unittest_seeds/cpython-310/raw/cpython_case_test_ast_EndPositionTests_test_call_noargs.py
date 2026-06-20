# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_call_noargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'x[0]()'
    call = self._parse_value(s)
    self._check_content(s, call.func, 'x[0]')
    self._check_end_pos(call, 1, 6)
