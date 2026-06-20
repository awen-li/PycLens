# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_attempting_to_send_to_non_generator

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
    try:
        gi = g()
        next(gi)
        for x in range(3):
            y = gi.send(42)
            trace.append('Should not have yielded: %s' % (y,))
    except AttributeError as e:
        self.assertIn('send', e.args[0])
    else:
        self.fail('was able to send into non-generator')
    self.assertEqual(trace, ['starting g', 'finishing g'])
