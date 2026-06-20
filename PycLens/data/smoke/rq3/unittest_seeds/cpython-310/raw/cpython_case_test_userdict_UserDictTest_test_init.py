# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userdict.py
# case: UserDictTest_test_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for kw in ('self', 'other', 'iterable'):
        self.assertEqual(list(collections.UserDict(**{kw: 42}).items()), [(kw, 42)])
    self.assertEqual(list(collections.UserDict({}, dict=42).items()), [('dict', 42)])
    self.assertEqual(list(collections.UserDict({}, dict=None).items()), [('dict', None)])
    self.assertEqual(list(collections.UserDict(dict={'a': 42}).items()), [('dict', {'a': 42})])
    self.assertRaises(TypeError, collections.UserDict, 42)
    self.assertRaises(TypeError, collections.UserDict, (), ())
    self.assertRaises(TypeError, collections.UserDict.__init__)
