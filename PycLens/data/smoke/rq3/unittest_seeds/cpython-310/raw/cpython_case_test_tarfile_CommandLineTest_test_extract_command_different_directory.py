# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: CommandLineTest_test_extract_command_different_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.make_simple_tarfile(tmpname)
    try:
        with os_helper.temp_cwd(tarextdir):
            out = self.tarfilecmd('-e', tmpname, 'spamdir')
        self.assertEqual(out, b'')
    finally:
        os_helper.rmtree(tarextdir)
