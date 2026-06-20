# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slot_shadows_class_variable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError) as cm:

        class X:
            __slots__ = ['foo']
            foo = None
    m = str(cm.exception)
    self.assertEqual("'foo' in __slots__ conflicts with class variable", m)
