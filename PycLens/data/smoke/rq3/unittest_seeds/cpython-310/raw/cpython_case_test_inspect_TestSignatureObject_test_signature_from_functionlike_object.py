# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_from_functionlike_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(a, b, *args, kwonly=True, kwonlyreq, **kwargs):
        pass

    class funclike:

        def __init__(self, func):
            self.__name__ = func.__name__
            self.__code__ = func.__code__
            self.__annotations__ = func.__annotations__
            self.__defaults__ = func.__defaults__
            self.__kwdefaults__ = func.__kwdefaults__
            self.func = func

        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)
    sig_func = inspect.Signature.from_callable(func)
    sig_funclike = inspect.Signature.from_callable(funclike(func))
    self.assertEqual(sig_funclike, sig_func)
    sig_funclike = inspect.signature(funclike(func))
    self.assertEqual(sig_funclike, sig_func)
    fl = funclike(func)
    del fl.__defaults__
    self.assertEqual(self.signature(fl), ((('args', ..., ..., 'var_positional'), ('kwargs', ..., ..., 'var_keyword')), ...))
    _orig_isdesc = inspect.ismethoddescriptor

    def _isdesc(obj):
        if hasattr(obj, '_builtinmock'):
            return True
        return _orig_isdesc(obj)
    with unittest.mock.patch('inspect.ismethoddescriptor', _isdesc):
        builtin_func = funclike(func)
        self.assertFalse(inspect.ismethoddescriptor(builtin_func))
        builtin_func._builtinmock = True
        self.assertTrue(inspect.ismethoddescriptor(builtin_func))
        self.assertEqual(inspect.signature(builtin_func), sig_func)
