# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_returning_value_from_delegated_throw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        try:
            trace.append('Starting g1')
            yield 'g1 ham'
            yield from g2()
            yield 'g1 eggs'
        finally:
            trace.append('Finishing g1')

    def g2():
        try:
            trace.append('Starting g2')
            yield 'g2 spam'
            yield 'g2 more spam'
        except LunchError:
            trace.append('Caught LunchError in g2')
            yield 'g2 lunch saved'
            yield 'g2 yet more spam'

    class LunchError(Exception):
        pass
    g = g1()
    for i in range(2):
        x = next(g)
        trace.append('Yielded %s' % (x,))
    e = LunchError('tomato ejected')
    g.throw(e)
    for x in g:
        trace.append('Yielded %s' % (x,))
    self.assertEqual(trace, ['Starting g1', 'Yielded g1 ham', 'Starting g2', 'Yielded g2 spam', 'Caught LunchError in g2', 'Yielded g2 yet more spam', 'Yielded g1 eggs', 'Finishing g1'])
