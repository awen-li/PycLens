# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_make_weak_valued_dict_misc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, weakref.WeakValueDictionary.__init__)
    self.assertRaises(TypeError, weakref.WeakValueDictionary, {}, {})
    self.assertRaises(TypeError, weakref.WeakValueDictionary, (), ())
    o = Object(3)
    for kw in ('self', 'dict', 'other', 'iterable'):
        d = weakref.WeakValueDictionary(**{kw: o})
        self.assertEqual(list(d.keys()), [kw])
        self.assertEqual(d[kw], o)
