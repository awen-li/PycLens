# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_value_attribute_of_StopIteration_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    trace = []

    def pex(e):
        trace.append('%s: %s' % (e.__class__.__name__, e))
        trace.append('value = %s' % (e.value,))
    e = StopIteration()
    pex(e)
    e = StopIteration('spam')
    pex(e)
    e.value = 'eggs'
    pex(e)
    self.assertEqual(trace, ['StopIteration: ', 'value = None', 'StopIteration: spam', 'value = spam', 'StopIteration: spam', 'value = eggs'])
