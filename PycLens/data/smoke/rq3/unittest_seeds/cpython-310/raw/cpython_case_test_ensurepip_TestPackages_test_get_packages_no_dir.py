# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestPackages_test_get_packages_no_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with unittest.mock.patch.object(ensurepip, '_PACKAGES', None), unittest.mock.patch.object(ensurepip, '_WHEEL_PKG_DIR', None):
        packages = ensurepip._get_packages()
        self.assertEqual(ensurepip._PIP_VERSION, ensurepip.version())
    self.assertIsNotNone(packages['pip'].wheel_name)
    self.assertIsNotNone(packages['setuptools'].wheel_name)
