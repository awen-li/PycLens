# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_conversion_of_sendNone_to_next

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g():
        yield from range(3)
    gi = g()
    for x in range(3):
        y = gi.send(None)
        trace.append('Yielded: %s' % (y,))
    self.assertEqual(trace, ['Yielded: 0', 'Yielded: 1', 'Yielded: 2'])
