# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_keyed_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = weakref.WeakKeyDictionary()
    o1 = Object('1')
    o2 = Object('2')
    d[o1] = 'something'
    d[o2] = 'something'
    self.assertEqual(len(d), 2)
    del d[o1]
    self.assertEqual(len(d), 1)
    self.assertEqual(list(d.keys()), [o2])
