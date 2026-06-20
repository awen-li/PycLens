# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_make_tarball

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (root_dir, base_dir) = self._create_files('')
    tmpdir2 = self.mkdtemp()
    os.rmdir(tmpdir2)
    work_dir = os.path.dirname(tmpdir2)
    rel_base_name = os.path.join(os.path.basename(tmpdir2), 'archive')
    with os_helper.change_cwd(work_dir), no_chdir:
        base_name = os.path.abspath(rel_base_name)
        tarball = make_archive(rel_base_name, 'gztar', root_dir, '.')
    self.assertEqual(tarball, base_name + '.tar.gz')
    self.assertTrue(os.path.isfile(tarball))
    self.assertTrue(tarfile.is_tarfile(tarball))
    with tarfile.open(tarball, 'r:gz') as tf:
        self.assertCountEqual(tf.getnames(), ['.', './sub', './sub2', './file1', './file2', './sub/file3'])
    with os_helper.change_cwd(work_dir), no_chdir:
        tarball = make_archive(rel_base_name, 'tar', root_dir, '.')
    self.assertEqual(tarball, base_name + '.tar')
    self.assertTrue(os.path.isfile(tarball))
    self.assertTrue(tarfile.is_tarfile(tarball))
    with tarfile.open(tarball, 'r') as tf:
        self.assertCountEqual(tf.getnames(), ['.', './sub', './sub2', './file1', './file2', './sub/file3'])
