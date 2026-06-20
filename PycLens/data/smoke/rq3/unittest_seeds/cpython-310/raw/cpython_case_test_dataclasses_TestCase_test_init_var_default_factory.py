# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_init_var_default_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'cannot have a default factory'):

        @dataclass
        class C:
            x: InitVar[int] = field(default_factory=int)
        self.assertNotIn('x', C.__dict__)
