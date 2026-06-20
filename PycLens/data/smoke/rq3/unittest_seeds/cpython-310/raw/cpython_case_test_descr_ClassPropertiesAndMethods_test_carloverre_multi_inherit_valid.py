# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_carloverre_multi_inherit_valid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(type):

        def __setattr__(cls, key, value):
            type.__setattr__(cls, key, value)

    class B:
        pass

    class C(B, A):
        pass
    obj = C('D', (object,), {})
    try:
        obj.test = True
    except TypeError:
        self.fail('setattr through direct base types should be legal')
