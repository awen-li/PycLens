# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_two_fields_one_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int = 0
    o = C(3)
    self.assertEqual((o.x, o.y), (3, 0))
    with self.assertRaisesRegex(TypeError, "non-default argument 'y' follows default argument"):

        @dataclass
        class C:
            x: int = 0
            y: int
    with self.assertRaisesRegex(TypeError, "non-default argument 'y' follows default argument"):

        @dataclass
        class B:
            x: int = 0

        @dataclass
        class C(B):
            y: int
    with self.assertRaisesRegex(TypeError, "non-default argument 'y' follows default argument"):

        @dataclass
        class B:
            x: int
            y: int

        @dataclass
        class C(B):
            x: int = 0
