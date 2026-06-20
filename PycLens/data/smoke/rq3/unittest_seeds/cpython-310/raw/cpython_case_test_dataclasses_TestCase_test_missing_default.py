# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_missing_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int = field(default=MISSING)
    with self.assertRaisesRegex(TypeError, '__init__\\(\\) missing 1 required positional argument'):
        C()
    self.assertNotIn('x', C.__dict__)

    @dataclass
    class D:
        x: int
    with self.assertRaisesRegex(TypeError, '__init__\\(\\) missing 1 required positional argument'):
        D()
    self.assertNotIn('x', D.__dict__)
