# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_object_new_and_init_with_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class OverrideNeither:
        pass
    self.assertRaises(TypeError, OverrideNeither, 1)
    self.assertRaises(TypeError, OverrideNeither, kw=1)

    class OverrideNew:

        def __new__(cls, foo, kw=0, *args, **kwds):
            return object.__new__(cls, *args, **kwds)

    class OverrideInit:

        def __init__(self, foo, kw=0, *args, **kwargs):
            return object.__init__(self, *args, **kwargs)

    class OverrideBoth(OverrideNew, OverrideInit):
        pass
    for case in (OverrideNew, OverrideInit, OverrideBoth):
        case(1)
        case(1, kw=2)
        self.assertRaises(TypeError, case, 1, 2, 3)
        self.assertRaises(TypeError, case, 1, 2, foo=3)
