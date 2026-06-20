# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_literal_eval_malformed_dict_nodes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    malformed = ast.Dict(keys=[ast.Constant(1), ast.Constant(2)], values=[ast.Constant(3)])
    self.assertRaises(ValueError, ast.literal_eval, malformed)
    malformed = ast.Dict(keys=[ast.Constant(1)], values=[ast.Constant(2), ast.Constant(3)])
    self.assertRaises(ValueError, ast.literal_eval, malformed)
