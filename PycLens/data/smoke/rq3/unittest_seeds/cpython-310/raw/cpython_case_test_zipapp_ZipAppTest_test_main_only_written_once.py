# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_main_only_written_once

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / 'foo.py').touch()
    (source / 'bar.py').touch()
    target = self.tmpdir / 'source.pyz'
    zipapp.create_archive(str(source), str(target), main='pkg.mod:fn')
    with zipfile.ZipFile(str(target), 'r') as z:
        self.assertEqual(1, z.namelist().count('__main__.py'))
