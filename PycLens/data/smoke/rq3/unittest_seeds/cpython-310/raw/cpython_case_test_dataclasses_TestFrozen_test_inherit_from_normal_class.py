# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestFrozen_test_inherit_from_normal_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for intermediate_class in [True, False]:
        with self.subTest(intermediate_class=intermediate_class):

            class C:
                pass
            if intermediate_class:

                class I(C):
                    pass
            else:
                I = C

            @dataclass(frozen=True)
            class D(I):
                i: int
        d = D(10)
        with self.assertRaises(FrozenInstanceError):
            d.i = 5
