# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestEq_test_no_eq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(eq=False)
    class C:
        x: int
    self.assertNotEqual(C(0), C(0))
    c = C(3)
    self.assertEqual(c, c)

    @dataclass(eq=False)
    class C:
        x: int

        def __eq__(self, other):
            return other == 10
    self.assertEqual(C(3), 10)
