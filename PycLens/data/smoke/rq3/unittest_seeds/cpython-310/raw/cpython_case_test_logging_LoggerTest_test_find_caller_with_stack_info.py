# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LoggerTest_test_find_caller_with_stack_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    called = []
    support.patch(self, logging.traceback, 'print_stack', lambda f, file: called.append(file.getvalue()))
    self.logger.findCaller(stack_info=True)
    self.assertEqual(len(called), 1)
    self.assertEqual('Stack (most recent call last):\n', called[0])
