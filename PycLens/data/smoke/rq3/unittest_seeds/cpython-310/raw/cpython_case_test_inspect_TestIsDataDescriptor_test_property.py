# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestIsDataDescriptor_test_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Propertied:

        @property
        def a_property(self):
            pass
    self.assertTrue(inspect.isdatadescriptor(Propertied.a_property), 'a property is a data descriptor')
