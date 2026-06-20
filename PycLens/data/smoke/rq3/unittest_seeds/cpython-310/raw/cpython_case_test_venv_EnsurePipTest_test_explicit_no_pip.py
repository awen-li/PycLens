# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: EnsurePipTest_test_explicit_no_pip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rmtree(self.env_dir)
    self.run_with_capture(venv.create, self.env_dir, with_pip=False)
    self.assert_pip_not_installed()
