# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ensurepip.py
# case: TestPackages_test_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as tmpdir:
        self.touch(tmpdir, 'pip-1.2.3b1-py2.py3-none-any.whl')
        self.touch(tmpdir, 'setuptools-49.1.3-py3-none-any.whl')
        with unittest.mock.patch.object(ensurepip, '_PACKAGES', None), unittest.mock.patch.object(ensurepip, '_WHEEL_PKG_DIR', tmpdir):
            self.assertEqual(ensurepip.version(), '1.2.3b1')
