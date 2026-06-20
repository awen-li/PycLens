# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestPackages_test_get_packages_with_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    setuptools_filename = 'setuptools-49.1.3-py3-none-any.whl'
    pip_filename = 'pip-20.2.2-py2.py3-none-any.whl'
    with tempfile.TemporaryDirectory() as tmpdir:
        self.touch(tmpdir, setuptools_filename)
        self.touch(tmpdir, pip_filename)
        self.touch(tmpdir, 'wheel-0.34.2-py2.py3-none-any.whl')
        with unittest.mock.patch.object(ensurepip, '_PACKAGES', None), unittest.mock.patch.object(ensurepip, '_WHEEL_PKG_DIR', tmpdir):
            packages = ensurepip._get_packages()
        self.assertEqual(packages['setuptools'].version, '49.1.3')
        self.assertEqual(packages['setuptools'].wheel_path, os.path.join(tmpdir, setuptools_filename))
        self.assertEqual(packages['pip'].version, '20.2.2')
        self.assertEqual(packages['pip'].wheel_path, os.path.join(tmpdir, pip_filename))
        self.assertEqual(sorted(packages), ['pip', 'setuptools'])
