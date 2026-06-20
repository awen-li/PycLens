# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_inherit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        i: int

    @dataclass(frozen=True)
    class D(C):
        j: int
    d = D(0, 10)
    with self.assertRaises(FrozenInstanceError):
        d.i = 5
    with self.assertRaises(FrozenInstanceError):
        d.j = 6
    self.assertEqual(d.i, 0)
    self.assertEqual(d.j, 10)
