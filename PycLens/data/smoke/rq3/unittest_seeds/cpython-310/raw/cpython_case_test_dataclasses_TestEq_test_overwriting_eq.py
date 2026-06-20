# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestEq_test_overwriting_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int

        def __eq__(self, other):
            return other == 3
    self.assertEqual(C(1), 3)
    self.assertNotEqual(C(1), 1)

    @dataclass(eq=True)
    class C:
        x: int

        def __eq__(self, other):
            return other == 4
    self.assertEqual(C(1), 4)
    self.assertNotEqual(C(1), 1)

    @dataclass(eq=False)
    class C:
        x: int

        def __eq__(self, other):
            return other == 5
    self.assertEqual(C(1), 5)
    self.assertNotEqual(C(1), 1)
