# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_valued_delitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = weakref.WeakValueDictionary()
    o1 = Object('1')
    o2 = Object('2')
    d['something'] = o1
    d['something else'] = o2
    self.assertEqual(len(d), 2)
    del d['something']
    self.assertEqual(len(d), 1)
    self.assertEqual(list(d.items()), [('something else', o2)])
