# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_init_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int = None
        init_param: InitVar[int] = None

        def __post_init__(self, init_param):
            if self.x is None:
                self.x = init_param * 2
    c = C(init_param=10)
    self.assertEqual(c.x, 20)
