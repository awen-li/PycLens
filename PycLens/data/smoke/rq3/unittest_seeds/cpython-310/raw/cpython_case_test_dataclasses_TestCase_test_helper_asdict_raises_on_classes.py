# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_helper_asdict_raises_on_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class C:
        x: int
        y: int
    with self.assertRaisesRegex(TypeError, 'dataclass instance'):
        asdict(C)
    with self.assertRaisesRegex(TypeError, 'dataclass instance'):
        asdict(int)
