# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_cause_and_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def inner_raise():
        try:
            self.zero_div()
        except ZeroDivisionError as _e:
            e = _e
        try:
            xyzzy
        except NameError:
            raise KeyError from e

    def outer_raise():
        inner_raise()
    blocks = boundaries.split(self.get_report(outer_raise))
    self.assertEqual(len(blocks), 3)
    self.assertEqual(blocks[1], cause_message)
    self.check_zero_div(blocks[0])
    self.assertIn('inner_raise() # Marker', blocks[2])
