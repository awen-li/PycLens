# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestUnique_test_unique_dirty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(ValueError, 'tres.*one'):

        @unique
        class Dirty(Enum):
            one = 1
            two = 'dos'
            tres = 1
    with self.assertRaisesRegex(ValueError, 'double.*single.*turkey.*triple'):

        @unique
        class Dirtier(IntEnum):
            single = 1
            double = 1
            triple = 3
            turkey = 3
