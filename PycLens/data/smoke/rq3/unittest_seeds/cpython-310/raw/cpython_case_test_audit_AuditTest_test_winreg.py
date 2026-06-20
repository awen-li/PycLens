# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_winreg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import_helper.import_module('winreg')
    (returncode, events, stderr) = self.run_python('test_winreg')
    if returncode:
        self.fail(stderr)
    self.assertEqual(events[0][0], 'winreg.OpenKey')
    self.assertEqual(events[1][0], 'winreg.OpenKey/result')
    expected = events[1][2]
    self.assertTrue(expected)
    self.assertSequenceEqual(['winreg.EnumKey', ' ', f'{expected} 0'], events[2])
    self.assertSequenceEqual(['winreg.EnumKey', ' ', f'{expected} 10000'], events[3])
    self.assertSequenceEqual(['winreg.PyHKEY.Detach', ' ', expected], events[4])
