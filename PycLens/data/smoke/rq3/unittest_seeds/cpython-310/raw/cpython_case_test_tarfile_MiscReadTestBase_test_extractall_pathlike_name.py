# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_extractall_pathlike_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DIR = pathlib.Path(TEMPDIR) / 'extractall'
    with os_helper.temp_dir(DIR), tarfile.open(tarname, encoding='iso8859-1') as tar:
        directories = [t for t in tar if t.isdir()]
        tar.extractall(DIR, directories, filter='fully_trusted')
        for tarinfo in directories:
            path = DIR / tarinfo.name
            self.assertEqual(os.path.getmtime(path), tarinfo.mtime)
