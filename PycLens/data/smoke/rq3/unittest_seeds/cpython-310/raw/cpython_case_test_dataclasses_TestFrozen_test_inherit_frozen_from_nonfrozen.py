# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_inherit_frozen_from_nonfrozen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for intermediate_class in [True, False]:
        with self.subTest(intermediate_class=intermediate_class):

            @dataclass
            class C:
                i: int
            if intermediate_class:

                class I(C):
                    pass
            else:
                I = C
            with self.assertRaisesRegex(TypeError, 'cannot inherit frozen dataclass from a non-frozen one'):

                @dataclass(frozen=True)
                class D(I):
                    pass
