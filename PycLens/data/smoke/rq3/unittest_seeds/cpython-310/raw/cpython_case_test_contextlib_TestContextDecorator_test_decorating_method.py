# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_decorating_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = mycontext()

    class Test(object):

        @context
        def method(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c
    test = Test()
    test.method(1, 2)
    self.assertEqual(test.a, 1)
    self.assertEqual(test.b, 2)
    self.assertEqual(test.c, None)
    test = Test()
    test.method('a', 'b', 'c')
    self.assertEqual(test.a, 'a')
    self.assertEqual(test.b, 'b')
    self.assertEqual(test.c, 'c')
    test = Test()
    test.method(a=1, b=2)
    self.assertEqual(test.a, 1)
    self.assertEqual(test.b, 2)
