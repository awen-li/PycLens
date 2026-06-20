# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_attr_passthrough

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        classvar = 4
    A = Annotated[C, 'a decoration']
    self.assertEqual(A.classvar, 4)
    A.x = 5
    self.assertEqual(C.x, 5)
