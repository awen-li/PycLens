# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_object_class_assignment_between_heaptypes_and_nonheaptypes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SubType(types.ModuleType):
        a = 1
    m = types.ModuleType('m')
    self.assertTrue(m.__class__ is types.ModuleType)
    self.assertFalse(hasattr(m, 'a'))
    m.__class__ = SubType
    self.assertTrue(m.__class__ is SubType)
    self.assertTrue(hasattr(m, 'a'))
    m.__class__ = types.ModuleType
    self.assertTrue(m.__class__ is types.ModuleType)
    self.assertFalse(hasattr(m, 'a'))

    class MyInt(int):
        __slots__ = ()
    with self.assertRaises(TypeError):
        1 .__class__ = MyInt

    class MyFloat(float):
        __slots__ = ()
    with self.assertRaises(TypeError):
        1.0.__class__ = MyFloat

    class MyComplex(complex):
        __slots__ = ()
    with self.assertRaises(TypeError):
        (1 + 2j).__class__ = MyComplex

    class MyStr(str):
        __slots__ = ()
    with self.assertRaises(TypeError):
        'a'.__class__ = MyStr

    class MyBytes(bytes):
        __slots__ = ()
    with self.assertRaises(TypeError):
        b'a'.__class__ = MyBytes

    class MyTuple(tuple):
        __slots__ = ()
    with self.assertRaises(TypeError):
        ().__class__ = MyTuple

    class MyFrozenSet(frozenset):
        __slots__ = ()
    with self.assertRaises(TypeError):
        frozenset().__class__ = MyFrozenSet
