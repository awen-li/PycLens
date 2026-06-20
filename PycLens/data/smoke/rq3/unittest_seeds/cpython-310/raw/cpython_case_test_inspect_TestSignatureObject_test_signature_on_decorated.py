# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_decorated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> int:
            return func(*args, **kwargs)
        return wrapper

    class Foo:

        @decorator
        def bar(self, a, b):
            pass
    bar = decorator(Foo().bar)
    self.assertEqual(self.signature(Foo.bar), ((('self', ..., ..., 'positional_or_keyword'), ('a', ..., ..., 'positional_or_keyword'), ('b', ..., ..., 'positional_or_keyword')), ...))
    self.assertEqual(self.signature(Foo().bar), ((('a', ..., ..., 'positional_or_keyword'), ('b', ..., ..., 'positional_or_keyword')), ...))
    self.assertEqual(self.signature(Foo.bar, follow_wrapped=False), ((('args', ..., ..., 'var_positional'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(bar), ((('a', ..., ..., 'positional_or_keyword'), ('b', ..., ..., 'positional_or_keyword')), ...))

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> int:
            return func(42, *args, **kwargs)
        sig = inspect.signature(func)
        new_params = tuple(sig.parameters.values())[1:]
        wrapper.__signature__ = sig.replace(parameters=new_params)
        return wrapper

    class Foo:

        @decorator
        def __call__(self, a, b):
            pass
    self.assertEqual(self.signature(Foo.__call__), ((('a', ..., ..., 'positional_or_keyword'), ('b', ..., ..., 'positional_or_keyword')), ...))
    self.assertEqual(self.signature(Foo().__call__), ((('b', ..., ..., 'positional_or_keyword'),), ...))

    def wrapped_foo_call():
        pass
    wrapped_foo_call.__wrapped__ = Foo.__call__
    self.assertEqual(self.signature(wrapped_foo_call), ((('a', ..., ..., 'positional_or_keyword'), ('b', ..., ..., 'positional_or_keyword')), ...))
