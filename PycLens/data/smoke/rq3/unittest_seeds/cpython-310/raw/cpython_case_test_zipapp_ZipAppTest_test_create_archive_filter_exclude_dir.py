# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_create_archive_filter_exclude_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def skip_dummy_dir(path):
        return path.parts[0] != 'dummy'
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    (source / 'test.py').touch()
    (source / 'dummy').mkdir()
    (source / 'dummy' / 'test2.py').touch()
    target = self.tmpdir / 'source.pyz'
    zipapp.create_archive(source, target, filter=skip_dummy_dir)
    with zipfile.ZipFile(target, 'r') as z:
        self.assertEqual(len(z.namelist()), 2)
        self.assertIn('__main__.py', z.namelist())
        self.assertIn('test.py', z.namelist())
