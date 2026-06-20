# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_singletons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for const in (None, False, True, Ellipsis, b'', frozenset()):
        with self.subTest(const=const):
            value = self.compile_constant(const)
            self.assertIs(value, const)
