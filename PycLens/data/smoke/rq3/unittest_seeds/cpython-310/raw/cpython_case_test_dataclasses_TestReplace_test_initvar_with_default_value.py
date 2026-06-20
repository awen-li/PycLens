# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_initvar_with_default_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: InitVar[int] = None
        z: InitVar[int] = 42

        def __post_init__(self, y, z):
            if y is not None:
                self.x += y
            if z is not None:
                self.x += z
    c = C(x=1, y=10, z=1)
    self.assertEqual(replace(c), C(x=12))
    self.assertEqual(replace(c, y=4), C(x=12, y=4, z=42))
    self.assertEqual(replace(c, y=4, z=1), C(x=12, y=4, z=1))
