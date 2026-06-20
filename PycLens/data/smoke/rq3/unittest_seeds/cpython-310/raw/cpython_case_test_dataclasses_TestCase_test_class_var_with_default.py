# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_class_var_with_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: ClassVar[int] = 10
    self.assertEqual(C.x, 10)

    @dataclass
    class C:
        x: ClassVar[int] = field(default=10)
    self.assertEqual(C.x, 10)
