# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegation_of_next_to_non_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g():
        yield from range(3)
    for x in g():
        trace.append('Yielded %s' % (x,))
    self.assertEqual(trace, ['Yielded 0', 'Yielded 1', 'Yielded 2'])
