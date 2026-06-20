# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_get_loader_avoids_emulation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with check_warnings() as w:
        self.assertIsNotNone(pkgutil.get_loader('sys'))
        self.assertIsNotNone(pkgutil.get_loader('os'))
        self.assertIsNotNone(pkgutil.get_loader('test.support'))
        self.assertEqual(len(w.warnings), 0)
