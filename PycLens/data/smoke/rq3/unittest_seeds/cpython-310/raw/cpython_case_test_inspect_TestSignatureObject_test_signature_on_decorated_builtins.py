# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_decorated_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    func = _testcapi.docstring_with_signature_with_defaults

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> int:
            return func(*args, **kwargs)
        return wrapper
    decorated_func = decorator(func)
    self.assertEqual(inspect.signature(func), inspect.signature(decorated_func))

    def wrapper_like(*args, **kwargs) -> int:
        pass
    self.assertEqual(inspect.signature(decorated_func, follow_wrapped=False), inspect.signature(wrapper_like))
