# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_exception_in_initial_next_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g1():
        trace.append('g1 about to yield from g2')
        yield from g2()
        trace.append('g1 should not be here')

    def g2():
        yield (1 / 0)

    def run():
        gi = g1()
        next(gi)
    self.assertRaises(ZeroDivisionError, run)
    self.assertEqual(trace, ['g1 about to yield from g2'])
