# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_mutable_bases_catch_mro_conflict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass

    class B(object):
        pass

    class C(A, B):
        pass

    class D(A, B):
        pass

    class E(C, D):
        pass
    try:
        C.__bases__ = (B, A)
    except TypeError:
        pass
    else:
        self.fail("didn't catch MRO conflict")
