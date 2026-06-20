# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    slc = ast.parse('x[::]').body[0].value.slice
    self.assertIsNone(slc.upper)
    self.assertIsNone(slc.lower)
    self.assertIsNone(slc.step)
