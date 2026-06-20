# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeConstsTest_test_interned_string_in_frozenset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    co = compile('res = a in {"str_value"}', '?', 'exec')
    v = self.find_const(co.co_consts, frozenset(('str_value',)))
    self.assertIsInterned(tuple(v)[0])
