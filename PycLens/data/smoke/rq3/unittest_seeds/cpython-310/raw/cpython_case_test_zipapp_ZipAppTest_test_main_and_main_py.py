# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_main_and_main_py

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = self.tmpdir / 'source.pyz'
    with self.assertRaises(zipapp.ZipAppError):
        zipapp.create_archive(str(source), str(target), main='pkg.mod:fn')
