# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_make_weak_valued_dict_from_weak_valued_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = Object(3)
    dict = weakref.WeakValueDictionary({364: o})
    dict2 = weakref.WeakValueDictionary(dict)
    self.assertEqual(dict[364], o)
