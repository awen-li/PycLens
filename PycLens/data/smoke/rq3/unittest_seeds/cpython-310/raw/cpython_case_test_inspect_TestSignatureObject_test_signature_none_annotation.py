# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_none_annotation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

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

    def foo():
        pass
    foo = funclike(foo)
    foo.__annotations__ = None
    for signature_func in (inspect.signature, inspect.Signature.from_callable):
        with self.subTest(signature_func=signature_func):
            self.assertEqual(signature_func(foo), inspect.Signature())
    self.assertEqual(inspect.get_annotations(foo), {})
