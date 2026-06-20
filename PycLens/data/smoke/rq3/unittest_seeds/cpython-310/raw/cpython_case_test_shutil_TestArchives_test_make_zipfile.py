# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_make_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (root_dir, base_dir) = self._create_files()
    tmpdir2 = self.mkdtemp()
    os.rmdir(tmpdir2)
    work_dir = os.path.dirname(tmpdir2)
    rel_base_name = os.path.join(os.path.basename(tmpdir2), 'archive')
    with os_helper.change_cwd(work_dir), no_chdir:
        base_name = os.path.abspath(rel_base_name)
        res = make_archive(rel_base_name, 'zip', root_dir)
    self.assertEqual(res, base_name + '.zip')
    self.assertTrue(os.path.isfile(res))
    self.assertTrue(zipfile.is_zipfile(res))
    with zipfile.ZipFile(res) as zf:
        self.assertCountEqual(zf.namelist(), ['dist/', 'dist/sub/', 'dist/sub2/', 'dist/file1', 'dist/file2', 'dist/sub/file3', 'outer'])
    with os_helper.change_cwd(work_dir), no_chdir:
        base_name = os.path.abspath(rel_base_name)
        res = make_archive(rel_base_name, 'zip', root_dir, base_dir)
    self.assertEqual(res, base_name + '.zip')
    self.assertTrue(os.path.isfile(res))
    self.assertTrue(zipfile.is_zipfile(res))
    with zipfile.ZipFile(res) as zf:
        self.assertCountEqual(zf.namelist(), ['dist/', 'dist/sub/', 'dist/sub2/', 'dist/file1', 'dist/file2', 'dist/sub/file3'])
