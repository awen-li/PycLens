# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    default = object()

    @dataclass
    class C:
        x: object = field(default=default)
    self.assertIs(C.x, default)
    c = C(10)
    self.assertEqual(c.x, 10)
    del c.x
    self.assertIs(c.x, default)
    self.assertIs(C().x, default)
