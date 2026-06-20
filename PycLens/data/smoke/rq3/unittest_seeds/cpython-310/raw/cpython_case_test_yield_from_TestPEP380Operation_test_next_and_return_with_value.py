# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_next_and_return_with_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def f(r):
        gi = g(r)
        next(gi)
        try:
            trace.append('f resuming g')
            next(gi)
            trace.append('f SHOULD NOT BE HERE')
        except StopIteration as e:
            trace.append('f caught %r' % (e,))

    def g(r):
        trace.append('g starting')
        yield
        trace.append('g returning %r' % (r,))
        return r
    f(None)
    f(1)
    f((2,))
    f(StopIteration(3))
    self.assertEqual(trace, ['g starting', 'f resuming g', 'g returning None', 'f caught StopIteration()', 'g starting', 'f resuming g', 'g returning 1', 'f caught StopIteration(1)', 'g starting', 'f resuming g', 'g returning (2,)', 'f caught StopIteration((2,))', 'g starting', 'f resuming g', 'g returning StopIteration(3)', 'f caught StopIteration(StopIteration(3))'])
