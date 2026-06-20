# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_make_archive_owner_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if UID_GID_SUPPORT:
        group = grp.getgrgid(0)[0]
        owner = pwd.getpwuid(0)[0]
    else:
        group = owner = 'root'
    (root_dir, base_dir) = self._create_files()
    base_name = os.path.join(self.mkdtemp(), 'archive')
    res = make_archive(base_name, 'zip', root_dir, base_dir, owner=owner, group=group)
    self.assertTrue(os.path.isfile(res))
    res = make_archive(base_name, 'zip', root_dir, base_dir)
    self.assertTrue(os.path.isfile(res))
    res = make_archive(base_name, 'tar', root_dir, base_dir, owner=owner, group=group)
    self.assertTrue(os.path.isfile(res))
    res = make_archive(base_name, 'tar', root_dir, base_dir, owner='kjhkjhkjg', group='oihohoh')
    self.assertTrue(os.path.isfile(res))
