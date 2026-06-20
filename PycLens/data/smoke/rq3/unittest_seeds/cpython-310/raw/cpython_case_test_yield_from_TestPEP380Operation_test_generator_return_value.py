# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_generator_return_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        trace.append('Starting g1')
        yield 'g1 ham'
        ret = (yield from g2())
        trace.append('g2 returned %r' % (ret,))
        for v in (1, (2,), StopIteration(3)):
            ret = (yield from g2(v))
            trace.append('g2 returned %r' % (ret,))
        yield 'g1 eggs'
        trace.append('Finishing g1')

    def g2(v=None):
        trace.append('Starting g2')
        yield 'g2 spam'
        yield 'g2 more spam'
        trace.append('Finishing g2')
        if v:
            return v
    for x in g1():
        trace.append('Yielded %s' % (x,))
    self.assertEqual(trace, ['Starting g1', 'Yielded g1 ham', 'Starting g2', 'Yielded g2 spam', 'Yielded g2 more spam', 'Finishing g2', 'g2 returned None', 'Starting g2', 'Yielded g2 spam', 'Yielded g2 more spam', 'Finishing g2', 'g2 returned 1', 'Starting g2', 'Yielded g2 spam', 'Yielded g2 more spam', 'Finishing g2', 'g2 returned (2,)', 'Starting g2', 'Yielded g2 spam', 'Yielded g2 more spam', 'Finishing g2', 'g2 returned StopIteration(3)', 'Yielded g1 eggs', 'Finishing g1'])
