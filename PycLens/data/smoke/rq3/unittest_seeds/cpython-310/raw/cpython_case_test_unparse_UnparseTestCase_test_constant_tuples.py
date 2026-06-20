# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_constant_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_src_roundtrip(ast.Constant(value=(1,), kind=None), '(1,)')
    self.check_src_roundtrip(ast.Constant(value=(1, 2, 3), kind=None), '(1, 2, 3)')
