# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_testcapi_no_segfault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        import _testcapi
    except ImportError:
        pass
    else:

        class X(object):
            p = property(_testcapi.test_with_docstring)
