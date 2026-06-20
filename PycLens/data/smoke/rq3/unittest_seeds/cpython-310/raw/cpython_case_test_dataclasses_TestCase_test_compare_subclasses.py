# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_compare_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class B:
        i: int

    @dataclass
    class C(B):
        pass
    for (idx, (fn, expected)) in enumerate([(lambda a, b: a == b, False), (lambda a, b: a != b, True)]):
        with self.subTest(idx=idx):
            self.assertEqual(fn(B(0), C(0)), expected)
    for (idx, fn) in enumerate([lambda a, b: a < b, lambda a, b: a <= b, lambda a, b: a > b, lambda a, b: a >= b]):
        with self.subTest(idx=idx):
            with self.assertRaisesRegex(TypeError, "not supported between instances of 'B' and 'C'"):
                fn(B(0), C(0))
