# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_tarfile_vs_tar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (root_dir, base_dir) = self._create_files()
    base_name = os.path.join(self.mkdtemp(), 'archive')
    with no_chdir:
        tarball = make_archive(base_name, 'gztar', root_dir, base_dir)
    self.assertEqual(tarball, base_name + '.tar.gz')
    self.assertTrue(os.path.isfile(tarball))
    tarball2 = os.path.join(root_dir, 'archive2.tar')
    tar_cmd = ['tar', '-cf', 'archive2.tar', base_dir]
    subprocess.check_call(tar_cmd, cwd=root_dir, stdout=subprocess.DEVNULL)
    self.assertTrue(os.path.isfile(tarball2))
    self.assertEqual(self._tarinfo(tarball), self._tarinfo(tarball2))
    with no_chdir:
        tarball = make_archive(base_name, 'tar', root_dir, base_dir)
    self.assertEqual(tarball, base_name + '.tar')
    self.assertTrue(os.path.isfile(tarball))
    with no_chdir:
        tarball = make_archive(base_name, 'tar', root_dir, base_dir, dry_run=True)
    self.assertEqual(tarball, base_name + '.tar')
    self.assertTrue(os.path.isfile(tarball))
