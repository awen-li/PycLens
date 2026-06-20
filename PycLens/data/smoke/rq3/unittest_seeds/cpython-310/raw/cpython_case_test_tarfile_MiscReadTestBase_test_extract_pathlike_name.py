# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscReadTestBase_test_extract_pathlike_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dirtype = 'ustar/dirtype'
    DIR = pathlib.Path(TEMPDIR) / 'extractall'
    with os_helper.temp_dir(DIR), tarfile.open(tarname, encoding='iso8859-1') as tar:
        tarinfo = tar.getmember(dirtype)
        tar.extract(tarinfo, path=DIR, filter='fully_trusted')
        extracted = DIR / dirtype
        self.assertEqual(os.path.getmtime(extracted), tarinfo.mtime)
