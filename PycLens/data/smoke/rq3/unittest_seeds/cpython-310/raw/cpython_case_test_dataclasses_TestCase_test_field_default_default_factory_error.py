# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_field_default_default_factory_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'cannot specify both default and default_factory'
    with self.assertRaisesRegex(ValueError, msg):

        @dataclass
        class C:
            x: int = field(default=1, default_factory=int)
