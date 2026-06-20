# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_0_field_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C0:
        pass

    @dataclass(order=False)
    class C1:
        pass
    for cls in [C0, C1]:
        with self.subTest(cls=cls):
            self.assertEqual(cls(), cls())
            for (idx, fn) in enumerate([lambda a, b: a < b, lambda a, b: a <= b, lambda a, b: a > b, lambda a, b: a >= b]):
                with self.subTest(idx=idx):
                    with self.assertRaisesRegex(TypeError, f"not supported between instances of '{cls.__name__}' and '{cls.__name__}'"):
                        fn(cls(), cls())

    @dataclass(order=True)
    class C:
        pass
    self.assertLessEqual(C(), C())
    self.assertGreaterEqual(C(), C())
