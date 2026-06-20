# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_initvar_is_specified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: InitVar[int]

        def __post_init__(self, y):
            self.x *= y
    c = C(1, 10)
    self.assertEqual(c.x, 10)
    with self.assertRaisesRegex(ValueError, "InitVar 'y' must be specified with replace()"):
        replace(c, x=3)
    c = replace(c, x=3, y=5)
    self.assertEqual(c.x, 15)
