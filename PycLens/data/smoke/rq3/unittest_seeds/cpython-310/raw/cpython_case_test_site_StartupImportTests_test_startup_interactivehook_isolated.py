# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: StartupImportTests_test_startup_interactivehook_isolated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = subprocess.Popen([sys.executable, '-I', '-c', 'import sys; sys.exit(hasattr(sys, "__interactivehook__"))']).wait()
    self.assertFalse(r, "'__interactivehook__' added in isolated mode")
