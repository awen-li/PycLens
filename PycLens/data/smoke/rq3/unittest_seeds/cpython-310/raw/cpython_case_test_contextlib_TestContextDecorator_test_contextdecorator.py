# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestContextDecorator_test_contextdecorator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    context = mycontext()
    with context as result:
        self.assertIs(result, context)
        self.assertTrue(context.started)
    self.assertEqual(context.exc, (None, None, None))
