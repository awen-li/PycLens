# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntFlag_test_multiple_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AllMixin:

        @classproperty
        def ALL(cls):
            members = list(cls)
            all_value = None
            if members:
                all_value = members[0]
                for member in members[1:]:
                    all_value |= member
            cls.ALL = all_value
            return all_value

    class StrMixin:

        def __str__(self):
            return self._name_.lower()

    class Color(AllMixin, IntFlag):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(Color.RED.value, 1)
    self.assertEqual(Color.GREEN.value, 2)
    self.assertEqual(Color.BLUE.value, 4)
    self.assertEqual(Color.ALL.value, 7)
    self.assertEqual(str(Color.BLUE), 'Color.BLUE')

    class Color(AllMixin, StrMixin, IntFlag):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(Color.RED.value, 1)
    self.assertEqual(Color.GREEN.value, 2)
    self.assertEqual(Color.BLUE.value, 4)
    self.assertEqual(Color.ALL.value, 7)
    self.assertEqual(str(Color.BLUE), 'blue')

    class Color(StrMixin, AllMixin, IntFlag):
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    self.assertEqual(Color.RED.value, 1)
    self.assertEqual(Color.GREEN.value, 2)
    self.assertEqual(Color.BLUE.value, 4)
    self.assertEqual(Color.ALL.value, 7)
    self.assertEqual(str(Color.BLUE), 'blue')
