# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_make_archive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmpdir = self.mkdtemp()
    base_name = os.path.join(tmpdir, 'archive')
    self.assertRaises(ValueError, make_archive, base_name, 'xxx')
