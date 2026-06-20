# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_unraisablehook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (returncode, events, stderr) = self.run_python('test_unraisablehook')
    if returncode:
        self.fail(stderr)
    self.assertEqual(events[0][0], 'sys.unraisablehook')
    self.assertEqual(events[0][2], "RuntimeError('nonfatal-error') Exception ignored for audit hook test")
