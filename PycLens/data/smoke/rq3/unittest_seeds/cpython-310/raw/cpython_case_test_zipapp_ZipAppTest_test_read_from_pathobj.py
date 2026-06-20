# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_read_from_pathobj

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target1 = self.tmpdir / 'target1.pyz'
    target2 = self.tmpdir / 'target2.pyz'
    zipapp.create_archive(source, target1, interpreter='python')
    zipapp.create_archive(target1, target2, interpreter='python2.7')
    self.assertEqual(zipapp.get_interpreter(target2), 'python2.7')
