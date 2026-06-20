# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegation_of_close_to_non_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def g():
        try:
            trace.append('starting g')
            yield from range(3)
            trace.append('g should not be here')
        finally:
            trace.append('finishing g')
    gi = g()
    next(gi)
    with captured_stderr() as output:
        gi.close()
    self.assertEqual(output.getvalue(), '')
    self.assertEqual(trace, ['starting g', 'finishing g'])
