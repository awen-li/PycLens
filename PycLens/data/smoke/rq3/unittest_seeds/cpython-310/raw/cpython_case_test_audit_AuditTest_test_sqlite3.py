# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_audit.py
# case: AuditTest_test_sqlite3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sqlite3 = import_helper.import_module('sqlite3')
    (returncode, events, stderr) = self.run_python('test_sqlite3')
    if returncode:
        self.fail(stderr)
    if support.verbose:
        print(*events, sep='\n')
    actual = [ev[0] for ev in events]
    expected = ['sqlite3.connect', 'sqlite3.connect/handle'] * 2
    if hasattr(sqlite3.Connection, 'enable_load_extension'):
        expected += ['sqlite3.enable_load_extension', 'sqlite3.load_extension']
    self.assertEqual(actual, expected)
