# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_decorator_with_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = mycontext()

    @context
    def test():
        self.assertIsNone(context.exc)
        self.assertTrue(context.started)
        raise NameError('foo')
    with self.assertRaisesRegex(NameError, 'foo'):
        test()
    self.assertIsNotNone(context.exc)
    self.assertIs(context.exc[0], NameError)
