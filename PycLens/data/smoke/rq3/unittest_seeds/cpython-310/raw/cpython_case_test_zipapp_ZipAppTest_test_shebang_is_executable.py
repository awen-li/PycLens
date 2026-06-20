# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_shebang_is_executable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = self.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), interpreter='python')
    self.assertTrue(target.stat().st_mode & stat.S_IEXEC)
