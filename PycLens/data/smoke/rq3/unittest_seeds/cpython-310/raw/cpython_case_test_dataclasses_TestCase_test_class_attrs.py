# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_class_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    default = object()

    @dataclass
    class C:
        x: int
        y: int = field(repr=False)
        z: object = default
        t: int = field(default=100)
    self.assertFalse(hasattr(C, 'x'))
    self.assertFalse(hasattr(C, 'y'))
    self.assertIs(C.z, default)
    self.assertEqual(C.t, 100)
