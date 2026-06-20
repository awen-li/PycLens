# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_properties_doc_attrib

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class E(object):

        def getter(self):
            """getter method"""
            return 0

        def setter(self_, value):
            """setter method"""
            pass
        prop = property(getter)
        self.assertEqual(prop.__doc__, 'getter method')
        prop2 = property(fset=setter)
        self.assertEqual(prop2.__doc__, None)
