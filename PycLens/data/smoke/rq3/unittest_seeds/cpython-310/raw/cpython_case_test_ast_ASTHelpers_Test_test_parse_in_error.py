# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTHelpers_Test_test_parse_in_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        1 / 0
    except Exception:
        with self.assertRaises(SyntaxError) as e:
            ast.literal_eval("'\\U'")
        self.assertIsNotNone(e.exception.__context__)
