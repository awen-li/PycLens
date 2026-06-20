# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_wrong_class_slot_wrapper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(int):
        __eq__ = str.__eq__
        __add__ = str.__add__
    a = A()
    with self.assertRaises(TypeError):
        a == a
    with self.assertRaises(TypeError):
        a + a
