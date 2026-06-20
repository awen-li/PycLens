# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_create_archive_with_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def skip_pyc_files(path):
        return path.suffix != '.pyc'
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    (source / 'test.py').touch()
    (source / 'test.pyc').touch()
    target = self.tmpdir / 'source.pyz'
    zipapp.create_archive(source, target, filter=skip_pyc_files)
    with zipfile.ZipFile(target, 'r') as z:
        self.assertIn('__main__.py', z.namelist())
        self.assertIn('test.py', z.namelist())
        self.assertNotIn('test.pyc', z.namelist())
