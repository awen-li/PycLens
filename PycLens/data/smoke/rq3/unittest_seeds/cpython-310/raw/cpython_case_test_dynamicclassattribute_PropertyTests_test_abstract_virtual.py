# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamicclassattribute.py
# case: PropertyTests_test_abstract_virtual

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, ClassWithAbstractVirtualProperty)
    self.assertRaises(TypeError, ClassWithPropertyAbstractVirtual)

    class APV(ClassWithPropertyAbstractVirtual):
        pass
    self.assertRaises(TypeError, APV)

    class AVP(ClassWithAbstractVirtualProperty):
        pass
    self.assertRaises(TypeError, AVP)

    class Okay1(ClassWithAbstractVirtualProperty):

        @DynamicClassAttribute
        def color(self):
            return self._color

        def __init__(self):
            self._color = 'cyan'
    with self.assertRaises(AttributeError):
        Okay1.color
    self.assertEqual(Okay1().color, 'cyan')

    class Okay2(ClassWithAbstractVirtualProperty):

        @DynamicClassAttribute
        def color(self):
            return self._color

        def __init__(self):
            self._color = 'magenta'
    with self.assertRaises(AttributeError):
        Okay2.color
    self.assertEqual(Okay2().color, 'magenta')
