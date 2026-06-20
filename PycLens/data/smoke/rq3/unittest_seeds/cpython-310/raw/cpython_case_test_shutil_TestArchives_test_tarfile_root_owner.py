# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_tarfile_root_owner

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (root_dir, base_dir) = self._create_files()
    base_name = os.path.join(self.mkdtemp(), 'archive')
    group = grp.getgrgid(0)[0]
    owner = pwd.getpwuid(0)[0]
    with os_helper.change_cwd(root_dir), no_chdir:
        archive_name = make_archive(base_name, 'gztar', root_dir, 'dist', owner=owner, group=group)
    self.assertTrue(os.path.isfile(archive_name))
    archive = tarfile.open(archive_name)
    try:
        for member in archive.getmembers():
            self.assertEqual(member.uid, 0)
            self.assertEqual(member.gid, 0)
    finally:
        archive.close()
