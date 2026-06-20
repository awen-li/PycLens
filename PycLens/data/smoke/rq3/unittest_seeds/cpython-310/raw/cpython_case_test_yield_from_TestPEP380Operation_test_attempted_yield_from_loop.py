# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_attempted_yield_from_loop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        trace.append('g1: starting')
        yield 'y1'
        trace.append('g1: about to yield from g2')
        yield from g2()
        trace.append('g1 should not be here')

    def g2():
        trace.append('g2: starting')
        yield 'y2'
        trace.append('g2: about to yield from g1')
        yield from gi
        trace.append('g2 should not be here')
    try:
        gi = g1()
        for y in gi:
            trace.append('Yielded: %s' % (y,))
    except ValueError as e:
        self.assertEqual(e.args[0], 'generator already executing')
    else:
        self.fail("subgenerator didn't raise ValueError")
    self.assertEqual(trace, ['g1: starting', 'Yielded: y1', 'g1: about to yield from g2', 'g2: starting', 'Yielded: y2', 'g2: about to yield from g1'])
