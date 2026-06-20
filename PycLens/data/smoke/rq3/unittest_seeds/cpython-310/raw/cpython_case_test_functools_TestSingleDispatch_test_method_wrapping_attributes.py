# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_method_wrapping_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        @functools.singledispatchmethod
        def func(self, arg: int) -> str:
            """My function docstring"""
            return str(arg)

        @functools.singledispatchmethod
        @classmethod
        def cls_func(cls, arg: int) -> str:
            """My function docstring"""
            return str(arg)

        @functools.singledispatchmethod
        @staticmethod
        def static_func(arg: int) -> str:
            """My function docstring"""
            return str(arg)
    for meth in (A.func, A().func, A.cls_func, A().cls_func, A.static_func, A().static_func):
        with self.subTest(meth=meth):
            self.assertEqual(meth.__doc__, 'My function docstring')
            self.assertEqual(meth.__annotations__['arg'], int)
    self.assertEqual(A.func.__name__, 'func')
    self.assertEqual(A().func.__name__, 'func')
    self.assertEqual(A.cls_func.__name__, 'cls_func')
    self.assertEqual(A().cls_func.__name__, 'cls_func')
    self.assertEqual(A.static_func.__name__, 'static_func')
    self.assertEqual(A().static_func.__name__, 'static_func')
