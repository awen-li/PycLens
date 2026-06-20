# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_cycle_through_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(dict):

        def __init__(self):
            dict.__init__(self)
            self.__dict__ = self
    x = X()
    x.attr = 42
    wr = weakref.ref(x)
    del x
    support.gc_collect()
    self.assertIsNone(wr())
    for o in gc.get_objects():
        self.assertIsNot(type(o), X)
