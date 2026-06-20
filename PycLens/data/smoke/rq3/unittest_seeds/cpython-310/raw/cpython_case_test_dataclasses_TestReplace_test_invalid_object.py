# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestReplace_test_invalid_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        x: int
        y: int
    with self.assertRaisesRegex(TypeError, 'dataclass instance'):
        replace(C, x=3)
    with self.assertRaisesRegex(TypeError, 'dataclass instance'):
        replace(0, x=3)
