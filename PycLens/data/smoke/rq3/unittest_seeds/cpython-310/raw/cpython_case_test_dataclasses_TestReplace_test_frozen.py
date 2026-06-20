# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_frozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        x: int
        y: int
        z: int = field(init=False, default=10)
        t: int = field(init=False, default=100)
    c = C(1, 2)
    c1 = replace(c, x=3)
    self.assertEqual((c.x, c.y, c.z, c.t), (1, 2, 10, 100))
    self.assertEqual((c1.x, c1.y, c1.z, c1.t), (3, 2, 10, 100))
    with self.assertRaisesRegex(ValueError, 'init=False'):
        replace(c, x=3, z=20, t=50)
    with self.assertRaisesRegex(ValueError, 'init=False'):
        replace(c, z=20)
        replace(c, x=3, z=20, t=50)
    with self.assertRaisesRegex(FrozenInstanceError, "cannot assign to field 'x'"):
        c1.x = 3
    with self.assertRaisesRegex(TypeError, "__init__\\(\\) got an unexpected keyword argument 'a'"):
        c1 = replace(c, x=20, a=5)
