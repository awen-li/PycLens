# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestBootstrap_test_altinstall_default_pip_conflict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        ensurepip.bootstrap(altinstall=True, default_pip=True)
    self.assertFalse(self.run_pip.called)
