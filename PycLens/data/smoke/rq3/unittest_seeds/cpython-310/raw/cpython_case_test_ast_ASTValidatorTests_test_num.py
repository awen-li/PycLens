# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_num

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class subint(int):
        pass

    class subfloat(float):
        pass

    class subcomplex(complex):
        pass
    for obj in ('0', 'hello'):
        self.expr(ast.Num(obj))
    for obj in (subint(), subfloat(), subcomplex()):
        self.expr(ast.Num(obj), 'invalid type', exc=TypeError)
