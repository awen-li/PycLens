# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_class_property_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        """First"""

        @classmethod
        @property
        def __doc__(cls):
            return 'Second'
    self.assertEqual(A.__doc__, 'Second')
