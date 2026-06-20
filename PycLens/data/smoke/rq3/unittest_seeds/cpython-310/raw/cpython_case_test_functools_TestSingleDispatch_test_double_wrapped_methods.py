# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_double_wrapped_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def classmethod_friendly_decorator(func):
        wrapped = func.__func__

        @classmethod
        @functools.wraps(wrapped)
        def wrapper(*args, **kwargs):
            return wrapped(*args, **kwargs)
        return wrapper

    class WithoutSingleDispatch:

        @classmethod
        @contextlib.contextmanager
        def cls_context_manager(cls, arg: int) -> str:
            try:
                yield str(arg)
            finally:
                return 'Done'

        @classmethod_friendly_decorator
        @classmethod
        def decorated_classmethod(cls, arg: int) -> str:
            return str(arg)

    class WithSingleDispatch:

        @functools.singledispatchmethod
        @classmethod
        @contextlib.contextmanager
        def cls_context_manager(cls, arg: int) -> str:
            """My function docstring"""
            try:
                yield str(arg)
            finally:
                return 'Done'

        @functools.singledispatchmethod
        @classmethod_friendly_decorator
        @classmethod
        def decorated_classmethod(cls, arg: int) -> str:
            """My function docstring"""
            return str(arg)
    with WithoutSingleDispatch.cls_context_manager(5) as foo:
        without_single_dispatch_foo = foo
    with WithSingleDispatch.cls_context_manager(5) as foo:
        single_dispatch_foo = foo
    self.assertEqual(without_single_dispatch_foo, single_dispatch_foo)
    self.assertEqual(single_dispatch_foo, '5')
    self.assertEqual(WithoutSingleDispatch.decorated_classmethod(5), WithSingleDispatch.decorated_classmethod(5))
    self.assertEqual(WithSingleDispatch.decorated_classmethod(5), '5')
    for method_name in ('cls_context_manager', 'decorated_classmethod'):
        with self.subTest(method=method_name):
            self.assertEqual(getattr(WithSingleDispatch, method_name).__name__, getattr(WithoutSingleDispatch, method_name).__name__)
            self.assertEqual(getattr(WithSingleDispatch(), method_name).__name__, getattr(WithoutSingleDispatch(), method_name).__name__)
    for meth in (WithSingleDispatch.cls_context_manager, WithSingleDispatch().cls_context_manager, WithSingleDispatch.decorated_classmethod, WithSingleDispatch().decorated_classmethod):
        with self.subTest(meth=meth):
            self.assertEqual(meth.__doc__, 'My function docstring')
            self.assertEqual(meth.__annotations__['arg'], int)
    self.assertEqual(WithSingleDispatch.cls_context_manager.__name__, 'cls_context_manager')
    self.assertEqual(WithSingleDispatch().cls_context_manager.__name__, 'cls_context_manager')
    self.assertEqual(WithSingleDispatch.decorated_classmethod.__name__, 'decorated_classmethod')
    self.assertEqual(WithSingleDispatch().decorated_classmethod.__name__, 'decorated_classmethod')
