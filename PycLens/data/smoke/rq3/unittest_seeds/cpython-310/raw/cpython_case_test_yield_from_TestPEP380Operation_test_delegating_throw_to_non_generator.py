# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegating_throw_to_non_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g():
        try:
            trace.append('Starting g')
            yield from range(10)
        finally:
            trace.append('Finishing g')
    try:
        gi = g()
        for i in range(5):
            x = next(gi)
            trace.append('Yielded %s' % (x,))
        e = ValueError('tomato ejected')
        gi.throw(e)
    except ValueError as e:
        self.assertEqual(e.args[0], 'tomato ejected')
    else:
        self.fail('subgenerator failed to raise ValueError')
    self.assertEqual(trace, ['Starting g', 'Yielded 0', 'Yielded 1', 'Yielded 2', 'Yielded 3', 'Yielded 4', 'Finishing g'])
