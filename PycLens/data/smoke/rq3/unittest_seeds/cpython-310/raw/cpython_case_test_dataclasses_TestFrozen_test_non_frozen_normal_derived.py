# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_non_frozen_normal_derived

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class D:
        x: int
        y: int = 10

    class S(D):
        pass
    s = S(3)
    self.assertEqual(s.x, 3)
    self.assertEqual(s.y, 10)
    s.cached = True
    with self.assertRaises(FrozenInstanceError):
        s.x = 5
    with self.assertRaises(FrozenInstanceError):
        s.y = 5
    self.assertEqual(s.x, 3)
    self.assertEqual(s.y, 10)
    self.assertEqual(s.cached, True)
