# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestInit_test_overwriting_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int

        def __init__(self, x):
            self.x = 2 * x
    self.assertEqual(C(3).x, 6)

    @dataclass(init=True)
    class C:
        x: int

        def __init__(self, x):
            self.x = 2 * x
    self.assertEqual(C(4).x, 8)

    @dataclass(init=False)
    class C:
        x: int

        def __init__(self, x):
            self.x = 2 * x
    self.assertEqual(C(5).x, 10)
