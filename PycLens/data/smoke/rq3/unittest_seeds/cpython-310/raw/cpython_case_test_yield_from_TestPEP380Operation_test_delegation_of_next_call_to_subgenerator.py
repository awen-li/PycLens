# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegation_of_next_call_to_subgenerator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        trace.append('Starting g1')
        yield 'g1 ham'
        yield from g2()
        yield 'g1 eggs'
        trace.append('Finishing g1')

    def g2():
        trace.append('Starting g2')
        yield 'g2 spam'
        yield 'g2 more spam'
        trace.append('Finishing g2')
    for x in g1():
        trace.append('Yielded %s' % (x,))
    self.assertEqual(trace, ['Starting g1', 'Yielded g1 ham', 'Starting g2', 'Yielded g2 spam', 'Yielded g2 more spam', 'Finishing g2', 'Yielded g1 eggs', 'Finishing g1'])
