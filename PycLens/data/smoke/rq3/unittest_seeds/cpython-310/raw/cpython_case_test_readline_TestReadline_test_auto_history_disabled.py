# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_readline.py
# case: TestReadline_test_auto_history_disabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = run_pty(self.auto_history_script.format(False))
    self.assertIn(b'History length: 0', output)
