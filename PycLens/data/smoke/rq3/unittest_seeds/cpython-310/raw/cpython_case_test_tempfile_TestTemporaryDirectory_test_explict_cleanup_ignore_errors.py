# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_explict_cleanup_ignore_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as working_dir:
        temp_dir = self.do_create(dir=working_dir, ignore_cleanup_errors=True)
        temp_path = pathlib.Path(temp_dir.name)
        self.assertTrue(temp_path.exists(), f'TemporaryDirectory {temp_path!s} does not exist')
        with open(temp_path / 'a_file.txt', 'w+t') as open_file:
            open_file.write('Hello world!\n')
            temp_dir.cleanup()
        self.assertEqual(len(list(temp_path.glob('*'))), int(sys.platform.startswith('win')), f'Unexpected number of files in TemporaryDirectory {temp_path!s}')
        self.assertEqual(temp_path.exists(), sys.platform.startswith('win'), f'TemporaryDirectory {temp_path!s} existence state unexpected')
        temp_dir.cleanup()
        self.assertFalse(temp_path.exists(), f'TemporaryDirectory {temp_path!s} exists after cleanup')
