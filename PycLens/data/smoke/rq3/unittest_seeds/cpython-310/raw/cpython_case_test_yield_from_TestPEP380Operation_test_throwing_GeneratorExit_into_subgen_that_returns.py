# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_throwing_GeneratorExit_into_subgen_that_returns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def f():
        try:
            trace.append('Enter f')
            yield
            trace.append('Exit f')
        except GeneratorExit:
            return

    def g():
        trace.append('Enter g')
        yield from f()
        trace.append('Exit g')
    try:
        gi = g()
        next(gi)
        gi.throw(GeneratorExit)
    except GeneratorExit:
        pass
    else:
        self.fail('subgenerator failed to raise GeneratorExit')
    self.assertEqual(trace, ['Enter g', 'Enter f'])
