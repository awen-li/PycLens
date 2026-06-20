# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_inherit_nonfrozen_from_empty_frozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(frozen=True)
    class C:
        pass
    with self.assertRaisesRegex(TypeError, 'cannot inherit non-frozen dataclass from a frozen one'):

        @dataclass
        class D(C):
            j: int
