# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_valued_dict_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_update(weakref.WeakValueDictionary, {1: C(), 'a': C(), C(): C()})
    self.assertRaises(TypeError, weakref.WeakValueDictionary.update)
    d = weakref.WeakValueDictionary()
    self.assertRaises(TypeError, d.update, {}, {})
    self.assertRaises(TypeError, d.update, (), ())
    self.assertEqual(list(d.keys()), [])
    o = Object(3)
    for kw in ('self', 'dict', 'other', 'iterable'):
        d = weakref.WeakValueDictionary()
        d.update(**{kw: o})
        self.assertEqual(list(d.keys()), [kw])
        self.assertEqual(d[kw], o)
