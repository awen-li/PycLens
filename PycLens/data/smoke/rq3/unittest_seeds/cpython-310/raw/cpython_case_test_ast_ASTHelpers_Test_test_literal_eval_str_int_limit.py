# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_literal_eval_str_int_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.adjust_int_max_str_digits(4000):
        ast.literal_eval('3' * 4000)
        with self.assertRaises(SyntaxError) as err_ctx:
            ast.literal_eval('3' * 4001)
        self.assertIn('Exceeds the limit ', str(err_ctx.exception))
        self.assertIn(' Consider hexadecimal ', str(err_ctx.exception))
