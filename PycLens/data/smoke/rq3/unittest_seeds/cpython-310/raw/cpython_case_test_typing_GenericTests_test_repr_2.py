# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_repr_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(Generic[T]):
        pass
    self.assertEqual(C.__module__, __name__)
    self.assertEqual(C.__qualname__, 'GenericTests.test_repr_2.<locals>.C')
    X = C[int]
    self.assertEqual(X.__module__, __name__)
    self.assertEqual(repr(X).split('.')[-1], 'C[int]')

    class Y(C[int]):
        pass
    self.assertEqual(Y.__module__, __name__)
    self.assertEqual(Y.__qualname__, 'GenericTests.test_repr_2.<locals>.Y')
