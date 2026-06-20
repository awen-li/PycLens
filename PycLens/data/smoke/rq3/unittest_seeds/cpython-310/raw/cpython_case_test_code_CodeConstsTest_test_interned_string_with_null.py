# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeConstsTest_test_interned_string_with_null

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    co = compile('res = "str\\0value!"', '?', 'exec')
    v = self.find_const(co.co_consts, 'str\x00value!')
    self.assertIsNotInterned(v)
