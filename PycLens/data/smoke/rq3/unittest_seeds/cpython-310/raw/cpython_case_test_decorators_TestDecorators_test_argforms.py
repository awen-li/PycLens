# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_argforms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def noteargs(*args, **kwds):

        def decorate(func):
            setattr(func, 'dbval', (args, kwds))
            return func
        return decorate
    args = ('Now', 'is', 'the', 'time')
    kwds = dict(one=1, two=2)

    @noteargs(*args, **kwds)
    def f1():
        return 42
    self.assertEqual(f1(), 42)
    self.assertEqual(f1.dbval, (args, kwds))

    @noteargs('terry', 'gilliam', eric='idle', john='cleese')
    def f2():
        return 84
    self.assertEqual(f2(), 84)
    self.assertEqual(f2.dbval, (('terry', 'gilliam'), dict(eric='idle', john='cleese')))

    @noteargs(1, 2)
    def f3():
        pass
    self.assertEqual(f3.dbval, ((1, 2), {}))
