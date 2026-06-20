# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userdict.py
# case: UserDictTest_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for kw in ('self', 'dict', 'other', 'iterable'):
        d = collections.UserDict()
        d.update(**{kw: 42})
        self.assertEqual(list(d.items()), [(kw, 42)])
    self.assertRaises(TypeError, collections.UserDict().update, 42)
    self.assertRaises(TypeError, collections.UserDict().update, {}, {})
    self.assertRaises(TypeError, collections.UserDict.update)
