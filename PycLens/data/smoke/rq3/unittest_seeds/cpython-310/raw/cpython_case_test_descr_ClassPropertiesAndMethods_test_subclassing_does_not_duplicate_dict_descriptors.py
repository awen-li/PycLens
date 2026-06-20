# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_subclassing_does_not_duplicate_dict_descriptors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base:
        pass

    class Sub(Base):
        pass
    self.assertIn('__dict__', Base.__dict__)
    self.assertNotIn('__dict__', Sub.__dict__)
