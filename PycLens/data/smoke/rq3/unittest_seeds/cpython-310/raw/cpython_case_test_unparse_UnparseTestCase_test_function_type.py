# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_function_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for function_type in ('() -> int', '(int, int) -> int', '(Callable[complex], More[Complex(call.to_typevar())]) -> None'):
        self.check_ast_roundtrip(function_type, mode='func_type')
