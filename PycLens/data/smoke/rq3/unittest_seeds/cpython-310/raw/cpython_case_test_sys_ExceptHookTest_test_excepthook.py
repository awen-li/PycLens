# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: ExceptHookTest_test_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with test.support.captured_output('stderr') as stderr:
        sys.excepthook(1, '1', 1)
    self.assertTrue('TypeError: print_exception(): Exception expected for value, str found' in stderr.getvalue())
