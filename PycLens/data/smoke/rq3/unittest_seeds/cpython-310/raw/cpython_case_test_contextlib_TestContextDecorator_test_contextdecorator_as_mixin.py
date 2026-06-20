# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_contextdecorator_as_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class somecontext(object):
        started = False
        exc = None

        def __enter__(self):
            self.started = True
            return self

        def __exit__(self, *exc):
            self.exc = exc

    class mycontext(somecontext, ContextDecorator):
        pass
    context = mycontext()

    @context
    def test():
        self.assertIsNone(context.exc)
        self.assertTrue(context.started)
    test()
    self.assertEqual(context.exc, (None, None, None))
