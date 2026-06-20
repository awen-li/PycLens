# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_init_var_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class Base:
        x: int
        init_base: InitVar[int]
    b = Base(0, 10)
    self.assertEqual(vars(b), {'x': 0})

    @dataclass
    class C(Base):
        y: int
        init_derived: InitVar[int]

        def __post_init__(self, init_base, init_derived):
            self.x = self.x + init_base
            self.y = self.y + init_derived
    c = C(10, 11, 50, 51)
    self.assertEqual(vars(c), {'x': 21, 'y': 101})
