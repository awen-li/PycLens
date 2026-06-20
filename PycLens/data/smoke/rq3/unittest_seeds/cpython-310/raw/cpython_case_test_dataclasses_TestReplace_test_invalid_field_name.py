# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_invalid_field_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        x: int
        y: int
    c = C(1, 2)
    with self.assertRaisesRegex(TypeError, "__init__\\(\\) got an unexpected keyword argument 'z'"):
        c1 = replace(c, z=3)
