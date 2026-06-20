# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_keyed_bad_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = weakref.WeakKeyDictionary()
    o = Object('1')
    self.assertRaises(KeyError, d.__delitem__, o)
    self.assertRaises(KeyError, d.__getitem__, o)
    self.assertRaises(TypeError, d.__delitem__, 13)
    self.assertRaises(TypeError, d.__getitem__, 13)
    self.assertRaises(TypeError, d.__setitem__, 13, 13)
