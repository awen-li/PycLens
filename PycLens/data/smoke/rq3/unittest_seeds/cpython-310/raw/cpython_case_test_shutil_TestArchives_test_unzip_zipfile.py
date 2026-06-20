# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestArchives_test_unzip_zipfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (root_dir, base_dir) = self._create_files()
    base_name = os.path.join(self.mkdtemp(), 'archive')
    with no_chdir:
        archive = make_archive(base_name, 'zip', root_dir, base_dir)
    self.assertEqual(archive, base_name + '.zip')
    self.assertTrue(os.path.isfile(archive))
    zip_cmd = ['unzip', '-t', archive]
    with os_helper.change_cwd(root_dir):
        try:
            subprocess.check_output(zip_cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            details = exc.output.decode(errors='replace')
            if 'unrecognized option: t' in details:
                self.skipTest("unzip doesn't support -t")
            msg = '{}\n\n**Unzip Output**\n{}'
            self.fail(msg.format(exc, details))
