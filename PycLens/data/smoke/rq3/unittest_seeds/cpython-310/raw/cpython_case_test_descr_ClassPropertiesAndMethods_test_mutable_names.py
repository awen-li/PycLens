# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_mutable_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        pass
    mod = C.__module__
    C.__name__ = 'D'
    self.assertEqual((C.__module__, C.__name__), (mod, 'D'))
    C.__name__ = 'D.E'
    self.assertEqual((C.__module__, C.__name__), (mod, 'D.E'))
