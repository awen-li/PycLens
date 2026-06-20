# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_find_caller_with_stacklevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    the_level = 1

    def innermost():
        self.logger.warning('test', stacklevel=the_level)

    def inner():
        innermost()

    def outer():
        inner()
    records = self.recording.records
    outer()
    self.assertEqual(records[-1].funcName, 'innermost')
    lineno = records[-1].lineno
    the_level += 1
    outer()
    self.assertEqual(records[-1].funcName, 'inner')
    self.assertGreater(records[-1].lineno, lineno)
    lineno = records[-1].lineno
    the_level += 1
    outer()
    self.assertEqual(records[-1].funcName, 'outer')
    self.assertGreater(records[-1].lineno, lineno)
    lineno = records[-1].lineno
    the_level += 1
    outer()
    self.assertEqual(records[-1].funcName, 'test_find_caller_with_stacklevel')
    self.assertGreater(records[-1].lineno, lineno)
