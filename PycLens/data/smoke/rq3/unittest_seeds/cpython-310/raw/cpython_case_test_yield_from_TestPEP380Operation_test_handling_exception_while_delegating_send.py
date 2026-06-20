# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_handling_exception_while_delegating_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        trace.append('Starting g1')
        x = (yield 'g1 ham')
        trace.append('g1 received %s' % (x,))
        yield from g2()
        x = (yield 'g1 eggs')
        trace.append('g1 received %s' % (x,))
        trace.append('Finishing g1')

    def g2():
        trace.append('Starting g2')
        x = (yield 'g2 spam')
        trace.append('g2 received %s' % (x,))
        raise ValueError('hovercraft is full of eels')
        x = (yield 'g2 more spam')
        trace.append('g2 received %s' % (x,))
        trace.append('Finishing g2')

    def run():
        g = g1()
        y = next(g)
        x = 1
        try:
            while 1:
                y = g.send(x)
                trace.append('Yielded %s' % (y,))
                x += 1
        except StopIteration:
            trace.append('StopIteration')
    self.assertRaises(ValueError, run)
    self.assertEqual(trace, ['Starting g1', 'g1 received 1', 'Starting g2', 'Yielded g2 spam', 'g2 received 2'])
