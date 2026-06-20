# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slots_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import abc

    class MyABC(metaclass=abc.ABCMeta):
        __slots__ = 'a'

    class Unrelated(object):
        pass
    MyABC.register(Unrelated)
    u = Unrelated()
    self.assertIsInstance(u, MyABC)
    self.assertRaises(TypeError, MyABC.a.__set__, u, 3)
