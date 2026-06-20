# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdout() as out:
        calendar.format(['1', '2', '3'], colwidth=3, spacing=1)
        self.assertEqual(out.getvalue().strip(), '1   2   3')
