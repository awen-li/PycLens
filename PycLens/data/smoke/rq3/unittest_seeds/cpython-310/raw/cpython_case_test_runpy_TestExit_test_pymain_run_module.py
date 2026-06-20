# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: TestExit_test_pymain_run_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ham = self.ham
    self.assertSigInt([sys.executable, '-m', ham.stem], cwd=ham.parent)
