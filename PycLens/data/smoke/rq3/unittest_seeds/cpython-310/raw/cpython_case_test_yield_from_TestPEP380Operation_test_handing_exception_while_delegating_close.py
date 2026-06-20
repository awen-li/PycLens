# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_handing_exception_while_delegating_close

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
            yield 'g2 more spam'
        finally:
            trace.append('Finishing g2')
            raise ValueError('nybbles have exploded with delight')
    try:
        g = g1()
        for i in range(2):
            x = next(g)
            trace.append('Yielded %s' % (x,))
        g.close()
    except ValueError as e:
        self.assertEqual(e.args[0], 'nybbles have exploded with delight')
        self.assertIsInstance(e.__context__, GeneratorExit)
    else:
        self.fail('subgenerator failed to raise ValueError')
    self.assertEqual(trace, ['Starting g1', 'Yielded g1 ham', 'Starting g2', 'Yielded g2 spam', 'Finishing g2', 'Finishing g1'])
