# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_nonhash_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AutoNumberInAList(Enum):

        def __new__(cls):
            value = [len(cls.__members__) + 1]
            obj = object.__new__(cls)
            obj._value_ = value
            return obj

    class ColorInAList(AutoNumberInAList):
        red = ()
        green = ()
        blue = ()
    self.assertEqual(list(ColorInAList), [ColorInAList.red, ColorInAList.green, ColorInAList.blue])
    for (enum, value) in zip(ColorInAList, range(3)):
        value += 1
        self.assertEqual(enum.value, [value])
        self.assertIs(ColorInAList([value]), enum)
