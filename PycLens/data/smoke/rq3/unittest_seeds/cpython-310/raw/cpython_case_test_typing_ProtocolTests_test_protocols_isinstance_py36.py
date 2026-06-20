# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_isinstance_py36

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class APoint:

        def __init__(self, x, y, label):
            self.x = x
            self.y = y
            self.label = label

    class BPoint:
        label = 'B'

        def __init__(self, x, y):
            self.x = x
            self.y = y

    class C:

        def __init__(self, attr):
            self.attr = attr

        def meth(self, arg):
            return 0

    class Bad:
        pass
    self.assertIsInstance(APoint(1, 2, 'A'), Point)
    self.assertIsInstance(BPoint(1, 2), Point)
    self.assertNotIsInstance(MyPoint(), Point)
    self.assertIsInstance(BPoint(1, 2), Position)
    self.assertIsInstance(Other(), Proto)
    self.assertIsInstance(Concrete(), Proto)
    self.assertIsInstance(C(42), Proto)
    self.assertNotIsInstance(Bad(), Proto)
    self.assertNotIsInstance(Bad(), Point)
    self.assertNotIsInstance(Bad(), Position)
    self.assertNotIsInstance(Bad(), Concrete)
    self.assertNotIsInstance(Other(), Concrete)
    self.assertIsInstance(NT(1, 2), Position)
