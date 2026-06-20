# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_del

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    thresholds = gc.get_threshold()
    gc.enable()
    gc.set_threshold(1)

    class A:

        def __del__(self):
            dir(self)
    a = A()
    del a
    gc.disable()
    gc.set_threshold(*thresholds)
