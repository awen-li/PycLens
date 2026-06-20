# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: RunStringTests_test_sys_exit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assert_run_failed(SystemExit):
        interpreters.run_string(self.id, dedent('\n                import sys\n                sys.exit()\n                '))
    with self.assert_run_failed(SystemExit, '42'):
        interpreters.run_string(self.id, dedent('\n                import sys\n                sys.exit(42)\n                '))
