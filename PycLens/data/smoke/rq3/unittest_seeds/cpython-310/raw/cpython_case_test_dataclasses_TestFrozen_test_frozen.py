# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_frozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        i: int
    c = C(10)
    self.assertEqual(c.i, 10)
    with self.assertRaises(FrozenInstanceError):
        c.i = 5
    self.assertEqual(c.i, 10)
