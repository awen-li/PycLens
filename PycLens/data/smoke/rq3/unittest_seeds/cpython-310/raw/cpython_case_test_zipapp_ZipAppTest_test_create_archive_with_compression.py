# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_create_archive_with_compression

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    (source / 'test.py').touch()
    target = self.tmpdir / 'source.pyz'
    zipapp.create_archive(source, target, compressed=True)
    with zipfile.ZipFile(target, 'r') as z:
        for name in ('__main__.py', 'test.py'):
            self.assertEqual(z.getinfo(name).compress_type, zipfile.ZIP_DEFLATED)
