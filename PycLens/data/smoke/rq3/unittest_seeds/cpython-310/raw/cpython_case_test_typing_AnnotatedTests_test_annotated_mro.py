# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_annotated_mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(Annotated[int, (1, 10)]):
        ...
    self.assertEqual(X.__mro__, (X, int, object), 'Annotated should be transparent.')
