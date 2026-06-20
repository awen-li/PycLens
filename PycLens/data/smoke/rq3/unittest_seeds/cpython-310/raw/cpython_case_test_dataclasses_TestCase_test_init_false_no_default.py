# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_init_false_no_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int = field(init=False)
    self.assertNotIn('x', C().__dict__)

    @dataclass
    class C:
        x: int
        y: int = 0
        z: int = field(init=False)
        t: int = 10
    self.assertNotIn('z', C(0).__dict__)
    self.assertEqual(vars(C(5)), {'t': 10, 'x': 5, 'y': 0})
