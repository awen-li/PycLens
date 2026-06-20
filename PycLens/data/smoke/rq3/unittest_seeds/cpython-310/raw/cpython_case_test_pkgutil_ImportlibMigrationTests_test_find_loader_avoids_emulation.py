# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_find_loader_avoids_emulation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with check_warnings() as w:
        self.assertIsNotNone(pkgutil.find_loader('sys'))
        self.assertIsNotNone(pkgutil.find_loader('os'))
        self.assertIsNotNone(pkgutil.find_loader('test.support'))
        self.assertEqual(len(w.warnings), 0)
