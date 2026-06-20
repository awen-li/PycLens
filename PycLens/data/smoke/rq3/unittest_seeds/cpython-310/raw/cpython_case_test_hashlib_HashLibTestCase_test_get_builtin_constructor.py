# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_get_builtin_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    get_builtin_constructor = getattr(hashlib, '__get_builtin_constructor')
    builtin_constructor_cache = getattr(hashlib, '__builtin_constructor_cache')
    self.assertRaises(ValueError, get_builtin_constructor, 'test')
    try:
        import _md5
    except ImportError:
        self.skipTest('_md5 module not available')
    sys.modules['_md5'] = None
    builtin_constructor_cache.clear()
    try:
        self.assertRaises(ValueError, get_builtin_constructor, 'md5')
    finally:
        if '_md5' in locals():
            sys.modules['_md5'] = _md5
        else:
            del sys.modules['_md5']
    self.assertRaises(TypeError, get_builtin_constructor, 3)
    constructor = get_builtin_constructor('md5')
    self.assertIs(constructor, _md5.md5)
    self.assertEqual(sorted(builtin_constructor_cache), ['MD5', 'md5'])
