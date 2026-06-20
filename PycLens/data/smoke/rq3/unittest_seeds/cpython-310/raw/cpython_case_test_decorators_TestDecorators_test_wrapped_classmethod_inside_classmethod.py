# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_wrapped_classmethod_inside_classmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyClassMethod1:

        def __init__(self, func):
            self.func = func

        def __call__(self, cls):
            if hasattr(self.func, '__get__'):
                return self.func.__get__(cls, cls)()
            return self.func(cls)

        def __get__(self, instance, owner=None):
            if owner is None:
                owner = type(instance)
            return MethodType(self, owner)

    class MyClassMethod2:

        def __init__(self, func):
            if isinstance(func, classmethod):
                func = func.__func__
            self.func = func

        def __call__(self, cls):
            return self.func(cls)

        def __get__(self, instance, owner=None):
            if owner is None:
                owner = type(instance)
            return MethodType(self, owner)
    for myclassmethod in [MyClassMethod1, MyClassMethod2]:

        class A:

            @myclassmethod
            def f1(cls):
                return cls

            @classmethod
            @myclassmethod
            def f2(cls):
                return cls

            @myclassmethod
            @classmethod
            def f3(cls):
                return cls

            @classmethod
            @classmethod
            def f4(cls):
                return cls

            @myclassmethod
            @MyClassMethod1
            def f5(cls):
                return cls

            @myclassmethod
            @MyClassMethod2
            def f6(cls):
                return cls
        self.assertIs(A.f1(), A)
        self.assertIs(A.f2(), A)
        self.assertIs(A.f3(), A)
        self.assertIs(A.f4(), A)
        self.assertIs(A.f5(), A)
        self.assertIs(A.f6(), A)
        a = A()
        self.assertIs(a.f1(), A)
        self.assertIs(a.f2(), A)
        self.assertIs(a.f3(), A)
        self.assertIs(a.f4(), A)
        self.assertIs(a.f5(), A)
        self.assertIs(a.f6(), A)

        def f(cls):
            return cls
        self.assertIs(myclassmethod(f).__get__(a)(), A)
        self.assertIs(myclassmethod(f).__get__(a, A)(), A)
        self.assertIs(myclassmethod(f).__get__(A, A)(), A)
        self.assertIs(myclassmethod(f).__get__(A)(), type(A))
        self.assertIs(classmethod(f).__get__(a)(), A)
        self.assertIs(classmethod(f).__get__(a, A)(), A)
        self.assertIs(classmethod(f).__get__(A, A)(), A)
        self.assertIs(classmethod(f).__get__(A)(), type(A))
