# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_list_command_invalid_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    zipname = support.findfile('zipdir.zip')
    (rc, out, err) = self.tarfilecmd_failure('-l', zipname)
    self.assertIn(b' is not a tar archive.', err)
    self.assertEqual(out, b'')
    self.assertEqual(rc, 1)
