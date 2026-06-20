# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_make_zipfile_in_curdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    root_dir = self.mkdtemp()
    with os_helper.change_cwd(root_dir), no_chdir:
        self.assertEqual(make_archive('test', 'zip'), 'test.zip')
        self.assertTrue(os.path.isfile('test.zip'))
