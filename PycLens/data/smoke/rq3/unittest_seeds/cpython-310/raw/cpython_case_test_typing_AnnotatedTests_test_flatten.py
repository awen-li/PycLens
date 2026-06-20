# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_flatten

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = Annotated[Annotated[int, 4], 5]
    self.assertEqual(A, Annotated[int, 4, 5])
    self.assertEqual(A.__metadata__, (4, 5))
    self.assertEqual(A.__origin__, int)
