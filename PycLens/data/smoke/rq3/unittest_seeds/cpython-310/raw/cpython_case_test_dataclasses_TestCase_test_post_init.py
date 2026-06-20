# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_post_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:

        def __post_init__(self):
            raise CustomError()
    with self.assertRaises(CustomError):
        C()

    @dataclass
    class C:
        i: int = 10

        def __post_init__(self):
            if self.i == 10:
                raise CustomError()
    with self.assertRaises(CustomError):
        C()
    C(5)

    @dataclass(init=False)
    class C:

        def __post_init__(self):
            raise CustomError()
    C()

    @dataclass
    class C:
        x: int = 0

        def __post_init__(self):
            self.x *= 2
    self.assertEqual(C().x, 0)
    self.assertEqual(C(2).x, 4)

    @dataclass(frozen=True)
    class C:
        x: int = 0

        def __post_init__(self):
            self.x *= 2
    with self.assertRaises(FrozenInstanceError):
        C()
