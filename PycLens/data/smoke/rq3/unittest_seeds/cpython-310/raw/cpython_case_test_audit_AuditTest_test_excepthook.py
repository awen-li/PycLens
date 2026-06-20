# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_excepthook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (returncode, events, stderr) = self.run_python('test_excepthook')
    if not returncode:
        self.fail(f'Expected fatal exception\n{stderr}')
    self.assertSequenceEqual([('sys.excepthook', ' ', "RuntimeError('fatal-error')")], events)
