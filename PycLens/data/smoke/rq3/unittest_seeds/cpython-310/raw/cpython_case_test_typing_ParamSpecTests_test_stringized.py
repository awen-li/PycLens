# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_stringized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')

    class C(Generic[P]):
        func: Callable['P', int]

        def foo(self, *args: 'P.args', **kwargs: 'P.kwargs'):
            pass
    self.assertEqual(gth(C, globals(), locals()), {'func': Callable[P, int]})
    self.assertEqual(gth(C.foo, globals(), locals()), {'args': P.args, 'kwargs': P.kwargs})
