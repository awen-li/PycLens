# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    with self.assertRaises(TypeError):
        Season.SPRING < Season.WINTER
    with self.assertRaises(TypeError):
        Season.SPRING > 4
    self.assertNotEqual(Season.SPRING, 1)

    class Part(Enum):
        SPRING = 1
        CLIP = 2
        BARREL = 3
    self.assertNotEqual(Season.SPRING, Part.SPRING)
    with self.assertRaises(TypeError):
        Season.SPRING < Part.CLIP
