# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_get_loader_handles_missing_loader_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global __loader__
    this_loader = __loader__
    del __loader__
    try:
        with check_warnings() as w:
            self.assertIsNotNone(pkgutil.get_loader(__name__))
            self.assertEqual(len(w.warnings), 0)
    finally:
        __loader__ = this_loader
