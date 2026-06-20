# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestSlots_test_returns_new_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        x: int
    B = dataclass(A, slots=True)
    self.assertIsNot(A, B)
    self.assertFalse(hasattr(A, '__slots__'))
    self.assertTrue(hasattr(B, '__slots__'))
