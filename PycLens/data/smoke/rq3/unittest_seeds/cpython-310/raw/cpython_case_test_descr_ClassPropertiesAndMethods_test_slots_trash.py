# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slots_trash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class trash(object):
        __slots__ = ['x']

        def __init__(self, x):
            self.x = x
    o = None
    for i in range(50000):
        o = trash(o)
    del o
