# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_bpo25750

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descr:
        __get__ = _testcapi.bad_get

    class X:
        descr = Descr()

        def __new__(cls):
            cls.descr = None
            cls.lst = [2 ** i for i in range(10000)]
    X.descr
