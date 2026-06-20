# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_test_command_invalid_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipname = support.findfile('zipdir.zip')
    (rc, out, err) = self.tarfilecmd_failure('-t', zipname)
    self.assertIn(b' is not a tar archive.', err)
    self.assertEqual(out, b'')
    self.assertEqual(rc, 1)
    for tar_name in testtarnames:
        with self.subTest(tar_name=tar_name):
            with open(tar_name, 'rb') as f:
                data = f.read()
            try:
                with open(tmpname, 'wb') as f:
                    f.write(data[:511])
                (rc, out, err) = self.tarfilecmd_failure('-t', tmpname)
                self.assertEqual(out, b'')
                self.assertEqual(rc, 1)
            finally:
                os_helper.unlink(tmpname)
