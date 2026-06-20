# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_evil_type_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Nasty(str):

        def __del__(self):
            C.__name__ = 'other'

    class C:
        pass
    C.__name__ = Nasty('abc')
    C.__name__ = 'normal'
