# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_temp_dir__existing_dir__quiet_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = tempfile.mkdtemp()
    path = os.path.realpath(path)
    try:
        with warnings_helper.check_warnings() as recorder:
            with os_helper.temp_dir(path, quiet=True) as temp_path:
                self.assertEqual(path, temp_path)
            warnings = [str(w.message) for w in recorder.warnings]
        self.assertTrue(os.path.isdir(path))
    finally:
        shutil.rmtree(path)
    self.assertEqual(len(warnings), 1, warnings)
    warn = warnings[0]
    self.assertTrue(warn.startswith(f'tests may fail, unable to create temporary directory {path!r}: '), warn)
