# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_cause_recursive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def inner_raise():
        try:
            try:
                self.zero_div()
            except ZeroDivisionError as e:
                z = e
                raise KeyError from e
        except KeyError as e:
            raise z from e

    def outer_raise():
        inner_raise()
    blocks = boundaries.split(self.get_report(outer_raise))
    self.assertEqual(len(blocks), 3)
    self.assertEqual(blocks[1], cause_message)
    self.assertIn('raise KeyError from e', blocks[0])
    self.assertNotIn('1/0', blocks[0])
    self.assertIn('inner_raise() # Marker', blocks[2])
    self.check_zero_div(blocks[2])
