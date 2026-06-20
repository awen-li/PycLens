# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegation_of_initial_next_to_subgenerator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        trace.append('Starting g1')
        yield from g2()
        trace.append('Finishing g1')

    def g2():
        trace.append('Starting g2')
        yield 42
        trace.append('Finishing g2')
    for x in g1():
        trace.append('Yielded %s' % (x,))
    self.assertEqual(trace, ['Starting g1', 'Starting g2', 'Yielded 42', 'Finishing g2', 'Finishing g1'])
