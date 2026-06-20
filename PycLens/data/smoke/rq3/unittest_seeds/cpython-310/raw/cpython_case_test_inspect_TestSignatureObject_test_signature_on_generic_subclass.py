# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_generic_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing import Generic, TypeVar
    T = TypeVar('T')

    class A(Generic[T]):

        def __init__(self, *, a: int) -> None:
            pass
    self.assertEqual(self.signature(A), ((('a', ..., int, 'keyword_only'),), None))
