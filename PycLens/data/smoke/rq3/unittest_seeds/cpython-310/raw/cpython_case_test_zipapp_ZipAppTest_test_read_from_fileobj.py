# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_read_from_fileobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = self.tmpdir / 'source.pyz'
    temp_archive = io.BytesIO()
    zipapp.create_archive(str(source), temp_archive, interpreter='python')
    new_target = io.BytesIO()
    temp_archive.seek(0)
    zipapp.create_archive(temp_archive, new_target, interpreter='python2.7')
    self.assertTrue(new_target.getvalue().startswith(b'#!python2.7\n'))
