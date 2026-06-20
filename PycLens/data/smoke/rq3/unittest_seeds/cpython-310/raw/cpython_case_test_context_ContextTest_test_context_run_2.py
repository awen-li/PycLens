# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_run_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = contextvars.Context()

    def func(*args, **kwargs):
        kwargs['spam'] = 'foo'
        args += ('bar',)
        return (args, kwargs)
    for f in (func, functools.partial(func)):
        self.assertEqual(ctx.run(f), (('bar',), {'spam': 'foo'}))
        self.assertEqual(ctx.run(f, 1), ((1, 'bar'), {'spam': 'foo'}))
        self.assertEqual(ctx.run(f, a=2), (('bar',), {'a': 2, 'spam': 'foo'}))
        self.assertEqual(ctx.run(f, 11, a=2), ((11, 'bar'), {'a': 2, 'spam': 'foo'}))
        a = {}
        self.assertEqual(ctx.run(f, 11, **a), ((11, 'bar'), {'spam': 'foo'}))
        self.assertEqual(a, {})
