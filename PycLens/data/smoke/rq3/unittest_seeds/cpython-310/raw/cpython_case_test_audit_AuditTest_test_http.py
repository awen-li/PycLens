# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_http

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import_helper.import_module('http.client')
    (returncode, events, stderr) = self.run_python('test_http_client')
    if returncode:
        self.fail(stderr)
    if support.verbose:
        print(*events, sep='\n')
    self.assertEqual(events[0][0], 'http.client.connect')
    self.assertEqual(events[0][2], 'www.python.org 80')
    self.assertEqual(events[1][0], 'http.client.send')
    if events[1][2] != '[cannot send]':
        self.assertIn('HTTP', events[1][2])
