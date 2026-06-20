# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestTemporaryDirectory_test_del_on_shutdown_ignore_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as working_dir:
        code = 'if True:\n                import pathlib\n                import sys\n                import tempfile\n                import warnings\n\n                temp_dir = tempfile.TemporaryDirectory(\n                    dir={working_dir!r}, ignore_cleanup_errors=True)\n                sys.stdout.buffer.write(temp_dir.name.encode())\n\n                temp_dir_2 = pathlib.Path(temp_dir.name) / "test_dir"\n                temp_dir_2.mkdir()\n                with open(temp_dir_2 / "test0.txt", "w") as test_file:\n                    test_file.write("Hello world!")\n                open_file = open(temp_dir_2 / "open_file.txt", "w")\n                open_file.write("Hello world!")\n\n                warnings.filterwarnings("always", category=ResourceWarning)\n                '.format(working_dir=working_dir)
        (__, out, err) = script_helper.assert_python_ok('-c', code)
        temp_path = pathlib.Path(out.decode().strip())
        self.assertEqual(len(list(temp_path.glob('*'))), int(sys.platform.startswith('win')), f'Unexpected number of files in TemporaryDirectory {temp_path!s}')
        self.assertEqual(temp_path.exists(), sys.platform.startswith('win'), f'TemporaryDirectory {temp_path!s} existence state unexpected')
        err = err.decode('utf-8', 'backslashreplace')
        self.assertNotIn('Exception', err)
        self.assertNotIn('Error', err)
        self.assertIn('ResourceWarning: Implicitly cleaning up', err)
