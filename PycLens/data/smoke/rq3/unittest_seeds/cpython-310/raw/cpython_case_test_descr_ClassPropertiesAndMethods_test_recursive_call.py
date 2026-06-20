# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_recursive_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        pass
    A.__call__ = A()
    try:
        A()()
    except RecursionError:
        pass
    else:
        self.fail('Recursion limit should have been reached for __call__()')
