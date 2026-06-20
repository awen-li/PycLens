# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_get_objects

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()
    l = []
    l.append(l)
    self.assertTrue(any((l is element for element in gc.get_objects(generation=0))))
    self.assertFalse(any((l is element for element in gc.get_objects(generation=1))))
    self.assertFalse(any((l is element for element in gc.get_objects(generation=2))))
    gc.collect(generation=0)
    self.assertFalse(any((l is element for element in gc.get_objects(generation=0))))
    self.assertTrue(any((l is element for element in gc.get_objects(generation=1))))
    self.assertFalse(any((l is element for element in gc.get_objects(generation=2))))
    gc.collect(generation=1)
    self.assertFalse(any((l is element for element in gc.get_objects(generation=0))))
    self.assertFalse(any((l is element for element in gc.get_objects(generation=1))))
    self.assertTrue(any((l is element for element in gc.get_objects(generation=2))))
    gc.collect(generation=2)
    self.assertFalse(any((l is element for element in gc.get_objects(generation=0))))
    self.assertFalse(any((l is element for element in gc.get_objects(generation=1))))
    self.assertTrue(any((l is element for element in gc.get_objects(generation=2))))
    del l
    gc.collect()
