# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_container_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        pass
    obj = C()
    ref = weakref.ref(obj)
    container = set([obj, 1])
    obj.x = iter(container)
    del obj, container
    gc.collect()
    self.assertTrue(ref() is None, 'Cycle was not collected')
