# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_is_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NotDataClass:
        pass
    self.assertFalse(is_dataclass(0))
    self.assertFalse(is_dataclass(int))
    self.assertFalse(is_dataclass(NotDataClass))
    self.assertFalse(is_dataclass(NotDataClass()))

    @dataclass
    class C:
        x: int

    @dataclass
    class D:
        d: C
        e: int
    c = C(10)
    d = D(c, 4)
    self.assertTrue(is_dataclass(C))
    self.assertTrue(is_dataclass(c))
    self.assertFalse(is_dataclass(c.x))
    self.assertTrue(is_dataclass(d.d))
    self.assertFalse(is_dataclass(d.e))
