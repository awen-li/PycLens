# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        def __init__(self):
            self.init = self.__init__
    a = A()
    gc.collect()
    del a
    self.assertNotEqual(gc.collect(), 0)
