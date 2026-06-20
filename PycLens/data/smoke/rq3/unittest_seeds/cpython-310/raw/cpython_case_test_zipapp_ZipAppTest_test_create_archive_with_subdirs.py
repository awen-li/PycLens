# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_create_archive_with_subdirs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    (source / 'foo').mkdir()
    (source / 'bar').mkdir()
    (source / 'foo' / '__init__.py').touch()
    target = io.BytesIO()
    zipapp.create_archive(str(source), target)
    target.seek(0)
    with zipfile.ZipFile(target, 'r') as z:
        self.assertIn('foo/', z.namelist())
        self.assertIn('bar/', z.namelist())
