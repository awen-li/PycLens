# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_threaded_weak_valued_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = weakref.WeakValueDictionary()
    with collect_in_thread():
        for i in range(100000):
            d[10] = RefCycle()
            x = d.pop(10, 10)
            self.assertIsNot(x, None)
