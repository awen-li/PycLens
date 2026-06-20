# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_not_in_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int = 0
        y: int = field(compare=False, default=4)
    self.assertEqual(C(), C(0, 20))
    self.assertEqual(C(1, 10), C(1, 20))
    self.assertNotEqual(C(3), C(4, 10))
    self.assertNotEqual(C(3, 10), C(4, 10))
