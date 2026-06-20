# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipapp.py
# case: ZipAppTest_test_content_of_copied_archive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = self.tmpdir / 'source'
    source.mkdir()
    (source / '__main__.py').touch()
    target = io.BytesIO()
    zipapp.create_archive(str(source), target, interpreter='python')
    new_target = io.BytesIO()
    target.seek(0)
    zipapp.create_archive(target, new_target, interpreter=None)
    new_target.seek(0)
    with zipfile.ZipFile(new_target, 'r') as z:
        self.assertEqual(set(z.namelist()), {'__main__.py'})
