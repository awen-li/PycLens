# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_concurrent_futures.py
# case: ExecutorTest_test_no_stale_references

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    my_object = MyObject()
    my_object_collected = threading.Event()
    my_object_callback = weakref.ref(my_object, lambda obj: my_object_collected.set())
    self.executor.submit(my_object.my_method)
    del my_object
    collected = my_object_collected.wait(timeout=support.SHORT_TIMEOUT)
    self.assertTrue(collected, 'Stale reference not collected within timeout.')
