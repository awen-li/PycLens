# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_1_field_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C0:
        x: int

    @dataclass(order=False)
    class C1:
        x: int
    for cls in [C0, C1]:
        with self.subTest(cls=cls):
            self.assertEqual(cls(1), cls(1))
            self.assertNotEqual(cls(0), cls(1))
            for (idx, fn) in enumerate([lambda a, b: a < b, lambda a, b: a <= b, lambda a, b: a > b, lambda a, b: a >= b]):
                with self.subTest(idx=idx):
                    with self.assertRaisesRegex(TypeError, f"not supported between instances of '{cls.__name__}' and '{cls.__name__}'"):
                        fn(cls(0), cls(0))

    @dataclass(order=True)
    class C:
        x: int
    self.assertLess(C(0), C(1))
    self.assertLessEqual(C(0), C(1))
    self.assertLessEqual(C(1), C(1))
    self.assertGreater(C(1), C(0))
    self.assertGreaterEqual(C(1), C(0))
    self.assertGreaterEqual(C(1), C(1))
