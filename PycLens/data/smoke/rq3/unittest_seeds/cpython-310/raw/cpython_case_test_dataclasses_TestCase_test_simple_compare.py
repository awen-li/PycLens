# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_simple_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C0:
        x: int
        y: int

    @dataclass(order=False)
    class C1:
        x: int
        y: int
    for cls in [C0, C1]:
        with self.subTest(cls=cls):
            self.assertEqual(cls(0, 0), cls(0, 0))
            self.assertEqual(cls(1, 2), cls(1, 2))
            self.assertNotEqual(cls(1, 0), cls(0, 0))
            self.assertNotEqual(cls(1, 0), cls(1, 1))
            for (idx, fn) in enumerate([lambda a, b: a < b, lambda a, b: a <= b, lambda a, b: a > b, lambda a, b: a >= b]):
                with self.subTest(idx=idx):
                    with self.assertRaisesRegex(TypeError, f"not supported between instances of '{cls.__name__}' and '{cls.__name__}'"):
                        fn(cls(0, 0), cls(0, 0))

    @dataclass(order=True)
    class C:
        x: int
        y: int
    for (idx, fn) in enumerate([lambda a, b: a == b, lambda a, b: a <= b, lambda a, b: a >= b]):
        with self.subTest(idx=idx):
            self.assertTrue(fn(C(0, 0), C(0, 0)))
    for (idx, fn) in enumerate([lambda a, b: a < b, lambda a, b: a <= b, lambda a, b: a != b]):
        with self.subTest(idx=idx):
            self.assertTrue(fn(C(0, 0), C(0, 1)))
            self.assertTrue(fn(C(0, 1), C(1, 0)))
            self.assertTrue(fn(C(1, 0), C(1, 1)))
    for (idx, fn) in enumerate([lambda a, b: a > b, lambda a, b: a >= b, lambda a, b: a != b]):
        with self.subTest(idx=idx):
            self.assertTrue(fn(C(0, 1), C(0, 0)))
            self.assertTrue(fn(C(1, 0), C(0, 1)))
            self.assertTrue(fn(C(1, 1), C(1, 0)))
