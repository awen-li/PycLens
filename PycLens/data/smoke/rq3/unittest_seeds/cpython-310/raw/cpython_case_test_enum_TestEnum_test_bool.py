# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Logic(Enum):
        true = True
        false = False
    self.assertTrue(Logic.true)
    self.assertTrue(Logic.false)

    class RealLogic(Enum):
        true = True
        false = False

        def __bool__(self):
            return bool(self._value_)
    self.assertTrue(RealLogic.true)
    self.assertFalse(RealLogic.false)

    class IntLogic(int, Enum):
        true = 1
        false = 0
    self.assertTrue(IntLogic.true)
    self.assertFalse(IntLogic.false)
