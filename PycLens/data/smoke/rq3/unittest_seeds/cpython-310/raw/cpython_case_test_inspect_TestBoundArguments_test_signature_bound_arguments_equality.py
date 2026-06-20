# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBoundArguments_test_signature_bound_arguments_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a):
        pass
    ba = inspect.signature(foo).bind(1)
    self.assertTrue(ba == ba)
    self.assertFalse(ba != ba)
    self.assertTrue(ba == ALWAYS_EQ)
    self.assertFalse(ba != ALWAYS_EQ)
    ba2 = inspect.signature(foo).bind(1)
    self.assertTrue(ba == ba2)
    self.assertFalse(ba != ba2)
    ba3 = inspect.signature(foo).bind(2)
    self.assertFalse(ba == ba3)
    self.assertTrue(ba != ba3)
    ba3.arguments['a'] = 1
    self.assertTrue(ba == ba3)
    self.assertFalse(ba != ba3)

    def bar(b):
        pass
    ba4 = inspect.signature(bar).bind(1)
    self.assertFalse(ba == ba4)
    self.assertTrue(ba != ba4)

    def foo(*, a, b):
        pass
    sig = inspect.signature(foo)
    ba1 = sig.bind(a=1, b=2)
    ba2 = sig.bind(b=2, a=1)
    self.assertTrue(ba1 == ba2)
    self.assertFalse(ba1 != ba2)
