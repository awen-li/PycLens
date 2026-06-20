# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a: int=1, *, b, c=None, **kwargs) -> 42:
        pass
    self.assertEqual(str(inspect.signature(foo)), '(a: int = 1, *, b, c=None, **kwargs) -> 42')

    def foo(a: int=1, *args, b, c=None, **kwargs) -> 42:
        pass
    self.assertEqual(str(inspect.signature(foo)), '(a: int = 1, *args, b, c=None, **kwargs) -> 42')

    def foo():
        pass
    self.assertEqual(str(inspect.signature(foo)), '()')

    def foo(a: list[str]) -> tuple[str, float]:
        pass
    self.assertEqual(str(inspect.signature(foo)), '(a: list[str]) -> tuple[str, float]')
    from typing import Tuple

    def foo(a: list[str]) -> Tuple[str, float]:
        pass
    self.assertEqual(str(inspect.signature(foo)), '(a: list[str]) -> Tuple[str, float]')
