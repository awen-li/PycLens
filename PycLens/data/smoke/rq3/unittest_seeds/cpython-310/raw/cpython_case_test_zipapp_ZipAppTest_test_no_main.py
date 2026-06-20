# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_no_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / 'foo.py').touch()
    target = self.tmpdir / 'source.pyz'
    with self.assertRaises(zipapp.ZipAppError):
        zipapp.create_archive(str(source), str(target))
