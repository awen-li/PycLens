# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_make_weak_keyed_dict_from_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = Object(3)
    dict = weakref.WeakKeyDictionary({o: 364})
    self.assertEqual(dict[o], 364)
