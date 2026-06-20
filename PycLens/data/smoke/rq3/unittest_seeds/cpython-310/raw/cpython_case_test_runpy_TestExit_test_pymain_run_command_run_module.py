# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: TestExit_test_pymain_run_command_run_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertSigInt([sys.executable, '-c', "import runpy; runpy.run_module('ham')"], cwd=self.ham.parent)
