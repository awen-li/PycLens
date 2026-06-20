# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_multiple_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MaxMixin:

        @classproperty
        def MAX(cls):
            max = len(cls)
            cls.MAX = max
            return max

    class StrMixin:

        def __str__(self):
            return self._name_.lower()

    class SomeEnum(Enum):

        def behavior(self):
            return 'booyah'

    class AnotherEnum(Enum):

        def behavior(self):
            return 'nuhuh!'

        def social(self):
            return "what's up?"

    class Color(MaxMixin, Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(Color.RED.value, 1)
    self.assertEqual(Color.GREEN.value, 2)
    self.assertEqual(Color.BLUE.value, 3)
    self.assertEqual(Color.MAX, 3)
    self.assertEqual(str(Color.BLUE), 'Color.BLUE')

    class Color(MaxMixin, StrMixin, Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(Color.RED.value, 1)
    self.assertEqual(Color.GREEN.value, 2)
    self.assertEqual(Color.BLUE.value, 3)
    self.assertEqual(Color.MAX, 3)
    self.assertEqual(str(Color.BLUE), 'blue')

    class Color(StrMixin, MaxMixin, Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(Color.RED.value, 1)
    self.assertEqual(Color.GREEN.value, 2)
    self.assertEqual(Color.BLUE.value, 3)
    self.assertEqual(Color.MAX, 3)
    self.assertEqual(str(Color.BLUE), 'blue')

    class CoolColor(StrMixin, SomeEnum, Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(CoolColor.RED.value, 1)
    self.assertEqual(CoolColor.GREEN.value, 2)
    self.assertEqual(CoolColor.BLUE.value, 3)
    self.assertEqual(str(CoolColor.BLUE), 'blue')
    self.assertEqual(CoolColor.RED.behavior(), 'booyah')

    class CoolerColor(StrMixin, AnotherEnum, Enum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(CoolerColor.RED.value, 1)
    self.assertEqual(CoolerColor.GREEN.value, 2)
    self.assertEqual(CoolerColor.BLUE.value, 3)
    self.assertEqual(str(CoolerColor.BLUE), 'blue')
    self.assertEqual(CoolerColor.RED.behavior(), 'nuhuh!')
    self.assertEqual(CoolerColor.RED.social(), "what's up?")

    class CoolestColor(StrMixin, SomeEnum, AnotherEnum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(CoolestColor.RED.value, 1)
    self.assertEqual(CoolestColor.GREEN.value, 2)
    self.assertEqual(CoolestColor.BLUE.value, 3)
    self.assertEqual(str(CoolestColor.BLUE), 'blue')
    self.assertEqual(CoolestColor.RED.behavior(), 'booyah')
    self.assertEqual(CoolestColor.RED.social(), "what's up?")

    class ConfusedColor(StrMixin, AnotherEnum, SomeEnum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(ConfusedColor.RED.value, 1)
    self.assertEqual(ConfusedColor.GREEN.value, 2)
    self.assertEqual(ConfusedColor.BLUE.value, 3)
    self.assertEqual(str(ConfusedColor.BLUE), 'blue')
    self.assertEqual(ConfusedColor.RED.behavior(), 'nuhuh!')
    self.assertEqual(ConfusedColor.RED.social(), "what's up?")

    class ReformedColor(StrMixin, IntEnum, SomeEnum, AnotherEnum):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(ReformedColor.RED.value, 1)
    self.assertEqual(ReformedColor.GREEN.value, 2)
    self.assertEqual(ReformedColor.BLUE.value, 3)
    self.assertEqual(str(ReformedColor.BLUE), 'blue')
    self.assertEqual(ReformedColor.RED.behavior(), 'booyah')
    self.assertEqual(ConfusedColor.RED.social(), "what's up?")
    self.assertTrue(issubclass(ReformedColor, int))
