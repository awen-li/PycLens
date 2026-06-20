# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_disallowed_mutable_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (typ, empty, non_empty) in [(list, [], [1]), (dict, {}, {0: 1}), (set, set(), set([1]))]:
        with self.subTest(typ=typ):
            with self.assertRaisesRegex(ValueError, f'mutable default {typ} for field x is not allowed'):

                @dataclass
                class Point:
                    x: typ = empty
            with self.assertRaisesRegex(ValueError, f'mutable default {typ} for field y is not allowed'):

                @dataclass
                class Point:
                    y: typ = non_empty

            class Subclass(typ):
                pass
            with self.assertRaisesRegex(ValueError, f"mutable default .*Subclass'> for field z is not allowed"):

                @dataclass
                class Point:
                    z: typ = Subclass()

            @dataclass
            class C:
                z: ClassVar[typ] = typ()

            @dataclass
            class C:
                x: ClassVar[typ] = Subclass()
