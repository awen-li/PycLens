# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: BaseExceptionReportingTests_test_context_suppression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        try:
            raise Exception
        except:
            raise ZeroDivisionError from None
    except ZeroDivisionError as _:
        e = _
    lines = self.get_report(e).splitlines()
    self.assertEqual(len(lines), 4)
    self.assertTrue(lines[0].startswith('Traceback'))
    self.assertTrue(lines[1].startswith('  File'))
    self.assertIn('ZeroDivisionError from None', lines[2])
    self.assertTrue(lines[3].startswith('ZeroDivisionError'))
