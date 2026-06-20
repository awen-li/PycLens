# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_socket

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import_helper.import_module('socket')
    (returncode, events, stderr) = self.run_python('test_socket')
    if returncode:
        self.fail(stderr)
    if support.verbose:
        print(*events, sep='\n')
    self.assertEqual(events[0][0], 'socket.gethostname')
    self.assertEqual(events[1][0], 'socket.__new__')
    self.assertEqual(events[2][0], 'socket.bind')
    self.assertTrue(events[2][2].endswith("('127.0.0.1', 8080)"))
