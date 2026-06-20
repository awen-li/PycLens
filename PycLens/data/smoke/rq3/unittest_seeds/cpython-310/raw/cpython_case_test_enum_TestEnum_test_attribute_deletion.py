# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_attribute_deletion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Season(Enum):
        SPRING = 1
        SUMMER = 2
        AUTUMN = 3
        WINTER = 4

        def spam(cls):
            pass
    self.assertTrue(hasattr(Season, 'spam'))
    del Season.spam
    self.assertFalse(hasattr(Season, 'spam'))
    with self.assertRaises(AttributeError):
        del Season.SPRING
    with self.assertRaises(AttributeError):
        del Season.DRY
    with self.assertRaises(AttributeError):
        del Season.SPRING.name
