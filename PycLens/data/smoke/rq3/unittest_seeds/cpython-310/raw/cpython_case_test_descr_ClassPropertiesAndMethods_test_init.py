# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo(object):

        def __init__(self):
            return 10
    try:
        Foo()
    except TypeError:
        pass
    else:
        self.fail('did not test __init__() for None return')
