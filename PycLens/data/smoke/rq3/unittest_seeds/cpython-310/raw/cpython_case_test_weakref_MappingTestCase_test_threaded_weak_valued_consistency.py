# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_threaded_weak_valued_consistency

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = weakref.WeakValueDictionary()
    with collect_in_thread():
        for i in range(200000):
            o = RefCycle()
            d[10] = o
            self.assertEqual(len(d), 1)
            o = None
