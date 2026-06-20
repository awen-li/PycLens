# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: NoneInfoExtractTests_test_extractall_none_mtime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    now = pathlib.Path(TEMPDIR).stat().st_mtime
    with self.extract_with_none('mtime') as DIR:
        for path in pathlib.Path(DIR).glob('**/*'):
            with self.subTest(path=path):
                try:
                    mtime = path.stat().st_mtime
                except OSError:
                    if not path.is_symlink():
                        raise
                else:
                    self.assertGreaterEqual(path.stat().st_mtime, now)
