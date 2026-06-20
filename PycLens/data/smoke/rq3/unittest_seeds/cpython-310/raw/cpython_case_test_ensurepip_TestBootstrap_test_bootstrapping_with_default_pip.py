# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestBootstrap_test_bootstrapping_with_default_pip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ensurepip.bootstrap(default_pip=True)
    self.assertNotIn('ENSUREPIP_OPTIONS', self.os_environ)
