# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: StartupImportTests_test_startup_interactivehook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = subprocess.Popen([sys.executable, '-c', 'import sys; sys.exit(hasattr(sys, "__interactivehook__"))']).wait()
    self.assertTrue(r, "'__interactivehook__' not added by site")
