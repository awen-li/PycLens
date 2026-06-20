# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: NoneInfoExtractTests_test_extractall_none_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dir_mode = pathlib.Path(TEMPDIR).stat().st_mode
    regular_file = pathlib.Path(TEMPDIR) / 'regular_file'
    regular_file.write_text('')
    regular_file_mode = regular_file.stat().st_mode
    with self.extract_with_none('mode') as DIR:
        for path in pathlib.Path(DIR).glob('**/*'):
            with self.subTest(path=path):
                if path.is_dir():
                    self.assertEqual(path.stat().st_mode, dir_mode)
                elif path.is_file():
                    self.assertEqual(path.stat().st_mode, regular_file_mode)
