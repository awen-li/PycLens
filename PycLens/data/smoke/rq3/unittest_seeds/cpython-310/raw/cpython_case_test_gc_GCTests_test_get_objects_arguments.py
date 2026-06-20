# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_get_objects_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()
    self.assertEqual(len(gc.get_objects()), len(gc.get_objects(generation=None)))
    self.assertRaises(ValueError, gc.get_objects, 1000)
    self.assertRaises(ValueError, gc.get_objects, -1000)
    self.assertRaises(TypeError, gc.get_objects, '1')
    self.assertRaises(TypeError, gc.get_objects, 1.234)
