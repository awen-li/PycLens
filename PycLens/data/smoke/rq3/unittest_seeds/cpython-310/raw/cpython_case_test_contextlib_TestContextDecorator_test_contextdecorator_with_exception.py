# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_contextdecorator_with_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = mycontext()
    with self.assertRaisesRegex(NameError, 'foo'):
        with context:
            raise NameError('foo')
    self.assertIsNotNone(context.exc)
    self.assertIs(context.exc[0], NameError)
    context = mycontext()
    context.catch = True
    with context:
        raise NameError('foo')
    self.assertIsNotNone(context.exc)
    self.assertIs(context.exc[0], NameError)
