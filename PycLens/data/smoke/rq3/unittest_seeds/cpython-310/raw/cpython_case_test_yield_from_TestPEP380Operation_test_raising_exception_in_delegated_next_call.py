# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_raising_exception_in_delegated_next_call

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
            raise ValueError('hovercraft is full of eels')
            yield 'g2 more spam'
        finally:
            trace.append('Finishing g2')
    try:
        for x in g1():
            trace.append('Yielded %s' % (x,))
    except ValueError as e:
        self.assertEqual(e.args[0], 'hovercraft is full of eels')
    else:
        self.fail('subgenerator failed to raise ValueError')
    self.assertEqual(trace, ['Starting g1', 'Yielded g1 ham', 'Starting g2', 'Yielded g2 spam', 'Finishing g2', 'Finishing g1'])
