# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_strptime_exception_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError) as e:
        time.strptime('', '%D')
    self.assertIs(e.exception.__suppress_context__, True)
    with self.assertRaises(ValueError) as e:
        time.strptime('19', '%Y %')
    self.assertIs(e.exception.__suppress_context__, True)
