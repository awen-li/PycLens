# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_functionlike_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(a, b, *args, kwonly=True, kwonlyreq, **kwargs):
        pass

    class funclike:

        def __init__(self, marker):
            pass
        __name__ = func.__name__
        __code__ = func.__code__
        __annotations__ = func.__annotations__
        __defaults__ = func.__defaults__
        __kwdefaults__ = func.__kwdefaults__
    self.assertEqual(str(inspect.signature(funclike)), '(marker)')
