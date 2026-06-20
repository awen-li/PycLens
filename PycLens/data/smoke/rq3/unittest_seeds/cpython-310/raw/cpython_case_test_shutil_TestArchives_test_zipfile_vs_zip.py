# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_zipfile_vs_zip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (root_dir, base_dir) = self._create_files()
    base_name = os.path.join(self.mkdtemp(), 'archive')
    with no_chdir:
        archive = make_archive(base_name, 'zip', root_dir, base_dir)
    self.assertEqual(archive, base_name + '.zip')
    self.assertTrue(os.path.isfile(archive))
    archive2 = os.path.join(root_dir, 'archive2.zip')
    zip_cmd = ['zip', '-q', '-r', 'archive2.zip', base_dir]
    subprocess.check_call(zip_cmd, cwd=root_dir, stdout=subprocess.DEVNULL)
    self.assertTrue(os.path.isfile(archive2))
    with zipfile.ZipFile(archive) as zf:
        names = zf.namelist()
    with zipfile.ZipFile(archive2) as zf:
        names2 = zf.namelist()
    self.assertEqual(sorted(names), sorted(names2))
