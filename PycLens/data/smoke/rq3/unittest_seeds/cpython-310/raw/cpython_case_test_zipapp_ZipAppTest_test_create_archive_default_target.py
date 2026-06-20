# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_create_archive_default_target

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    zipapp.create_archive(str(source))
    expected_target = self.tmpdir / 'source.pyz'
    self.assertTrue(expected_target.is_file())
