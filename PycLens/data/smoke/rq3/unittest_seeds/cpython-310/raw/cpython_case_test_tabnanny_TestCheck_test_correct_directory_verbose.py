# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tabnanny.py
# case: TestCheck_test_correct_directory_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tempfile.TemporaryDirectory() as tmp_dir:
        lines = [f'{tmp_dir!r}: listing directory\n']
        file1 = TemporaryPyFile(SOURCE_CODES['error_free'], directory=tmp_dir)
        file2 = TemporaryPyFile(SOURCE_CODES['error_free'], directory=tmp_dir)
        with file1 as file1_path, file2 as file2_path:
            for file_path in (file1_path, file2_path):
                lines.append(f'{file_path!r}: Clean bill of health.\n')
            tabnanny.verbose = 1
            with captured_stdout() as stdout, captured_stderr() as stderr:
                tabnanny.check(tmp_dir)
            stdout = stdout.getvalue()
            for line in lines:
                with self.subTest(line=line):
                    self.assertIn(line, stdout)
            self.assertEqual(stderr.getvalue(), '')
